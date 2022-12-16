from pwn import *
from os import urandom
host,port = '65.2.136.80', 31092
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
io = remote(host,port)
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

io = remote(host,port)
io.recvuntil(b'4.exit')
io.sendline('3')
io.recvuntil(b'further')
io.sendline(iv_dec)
io.recvuntil(b'messages\n')
io.sendline('0')
io.recvline()
msg2 = msg1+tag1
io.recvline()
io.sendline(msg2)
io.recvline()
io.recvline()
tag2 = (io.recvline().decode())[:-1]


io = remote(host,port)
io.recvuntil(b'4.exit')
io.sendline('3')
io.recvuntil(b'further')
io.sendline(iv_dec)
io.recvuntil(b'messages\n')
io.sendline('0')
io.recvline()
msg2 = msg1+tag1
io.recvline()
io.sendline(msg2)
io.recvline()
io.recvline()
tag2 = (io.recvline().decode())[:-1]

io = remote(host,port)
io.recvuntil(b'4.exit')
io.sendline('3')
io.recvuntil(b'further')
io.sendline(iv_dec)
io.recvuntil(b'messages\n')
io.sendline('0')
io.recvline()
msg3 = msg2 + tag2
io.recvline()
io.sendline(msg2)
io.recvline()
io.recvline()
tag3 = (io.recvline().decode())[:-1]

io = remote(host,port)
io.recvuntil(b'4.exit')
io.sendline('3')
io.recvuntil(b'further')
io.sendline(iv_dec)
io.recvuntil(b'messages\n')
io.sendline('1')
io.recvuntil(b'Message #1: \n')
io.sendline(msg2)
io.recvuntil(b'Message #2: \n')
io.sendline(msg3)
io.recvline()
