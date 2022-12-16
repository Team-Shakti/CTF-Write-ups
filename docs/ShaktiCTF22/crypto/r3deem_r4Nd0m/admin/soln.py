from pwn import *
from Crypto.Util.number import *
host,port = '0.0.0.0',4929
io = remote(host,port)

io.recvuntil(b'provided\n')
n = int(io.recvline()[4:-1])
e = int(io.recvline()[4:-1])
h = int(io.recvline()[4:-1])
ct = int(io.recvline()[4:-1])
io.recvuntil(b'values\n')
io.sendline('1')
sp = int(io.recvline()[5:-1])
sq = int(io.recvline()[5:-1])
sr = int(io.recvline()[5:-1])
s1 = int(io.recvline()[5:-1])
s2 = int(io.recvline()[5:-1])
s3 = int(io.recvline()[5:-1])
s = int(io.recvline()[4:-1])

sp1 = sp+2      #create faults value one each time
sq1 = sq+2      #create faults value
sr1 = sr+2

io = remote(host,port)    
io.recvuntil(b'provided\n')
n = int(io.recvline()[4:-1])
e = int(io.recvline()[4:-1])
h = int(io.recvline()[4:-1])
io.recvuntil(b'values\n')
io.sendline('2')
io.recvuntil(b'sp value: ')
io.sendline(str(sp1))
io.recvuntil(b'sq value: ')
io.sendline(str(sq))
io.recvuntil(b'sr value: ')
io.sendline(str(sr))

s1 = int(io.recvline()[5:-1])
s2 = int(io.recvline()[5:-1])
s3 = int(io.recvline()[5:-1])
s = int(io.recvline()[4:-1]) 

qr = GCD((s**e)-h , n )

io = remote(host,port)    
io.recvuntil(b'provided\n')
n = int(io.recvline()[4:-1])
e = int(io.recvline()[4:-1])
h = int(io.recvline()[4:-1])
io.recvuntil(b'values\n')
io.sendline('2')
io.recvuntil(b'sp value: ')
io.sendline(str(sp))
io.recvuntil(b'sq value: ')
io.sendline(str(sq1))
io.recvuntil(b'sr value: ')
io.sendline(str(sr))

s1 = int(io.recvline()[5:-1])
s2 = int(io.recvline()[5:-1])
s3 = int(io.recvline()[5:-1])
s = int(io.recvline()[4:-1]) 

pr = GCD((s**e)-h , n)


io = remote(host,port)    
io.recvuntil(b'provided\n')
n = int(io.recvline()[4:-1])
e = int(io.recvline()[4:-1])
h = int(io.recvline()[4:-1])
io.recvuntil(b'values\n')
io.sendline('2')
io.recvuntil(b'sp value: ')
io.sendline(str(sp))
io.recvuntil(b'sq value: ')
io.sendline(str(sq))
io.recvuntil(b'sr value: ')
io.sendline(str(sr1))
s1 = int(io.recvline()[5:-1])
s2 = int(io.recvline()[5:-1])
s3 = int(io.recvline()[5:-1])
s = int(io.recvline()[4:-1]) 

pq = GCD((s**e)-h , n)

p = GCD(pq,pr)
q = GCD(pq,qr)
r = GCD(pr,qr)     


phi = (p-1)*(q-1)*(r-1)
d = inverse(e,phi)
pt = long_to_bytes(pow(ct,d,n))

print(pt)