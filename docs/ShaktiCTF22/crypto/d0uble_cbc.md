## d0uble_cbc

### Challenge Description :
My uncle has been working as a schoolteacher. One fine day, he decides to give chocolates to all his students. He brought a different types of chocolates. But two students are asking for the same kind of chocolate. All chocolates of that kind are completed except one. So, he decided to change the chocolate wrapper and give the same chocolate that he has.Can you help him to find that same chocolate wrapper?
### Difficulty Level
Medium


### Author
[b4b7gr00t](https://twitter.com/Paavani21)

### Points
200

### Flag format 
shaktictf{...}

### Writeup
1. This chall is combination of two iv detection in cbc mode and cbc mac vulnerability with non zero IV.
2. Find iv using the oracle provided and use that iv as input for cbc mac oracle.
3. iv detection can done by encrypting the `pt='\x00'*32` , decrypt `ct = b"\x00"*16+bytes.fromhex(ct)[:16]` , decrypt the result again to get iv. 

```python
from pwn import *
from os import urandom
host,port = '65.2.136.80',31351
io = remote(host,port)

io.recvuntil(b'4.exit')
io.sendline('1')
io.recvuntil(b'format\n')
pt = '\x00'*32
io.sendline(pt.encode().hex())
io.recvline()
ct = io.recvline()
ct = ct[25:-1].decode()
# host,port = '0.0.0.0',4304
io = remote(host,port)

io.recvuntil(b'4.exit')
io.sendline('2')
io.recvuntil(b'decrypt')
io.sendline(ct)
io.recvline()
pt = io.recvline()[28:-1]
ct = b"\x00"*16+bytes.fromhex(ct)[:16]

io = remote(host,port)
io.recvuntil(b'4.exit')
io.sendline('2')
io.recvuntil(b'decrypt')
io.sendline(ct.hex())
io.recvline()
iv_dec = (bytes.fromhex(io.recvline()[28:-1].decode())[16:]).hex()
```

5. Now pass that iv to the sign function. It will return the tag as ct[16:].
```python
io.recvuntil(b'4.exit')
io.sendline('3')
io.recvuntil(b'further')
io.sendline(iv_dec)
io.recvuntil(b'messages\n')
io.sendline('0')
io.recvline()
msg1 = urandom(16).hex()
io.recvline()
io.sendline(msg1)
io.recvline()
io.recvline()
tag1 = (io.recvline().decode())[:-1]
```
6. sign funtion is returning the last 16 bytes from `ct`. 


7. sign(sign(block0) xor block1) gives the same sign value. (So, simply append the ciphertext of the previous block)

For whole script refer [here](https://github.com/Paavani-git/ShaktiCTF22/blob/main/Double_cbc/Admin/soln.py)

#### Flag
`shaktictf{double_cheese_double_mac_yummyyyy_4120686170707920636263206d6f6465}`

