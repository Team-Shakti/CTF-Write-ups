# Simple_cipher

## points : 150

## Description:

We have a flag encrypted using this program. Can you figure out what it is?

## Writeup

The challenge is basically a xoring challenge where random numbers gets xored with the input to form the encrypted key provided in the file named flag.enc

Going through the debuggers , we can see that there is a call of :srand(0x1337) 
The srand() function sets the starting point for for the production of random numbers . It also got two xoring operations .Hence xorring with the random numbers and the data from the flag.enc to get the flag

#### Solution Script

```py
import random
from ctypes import CDLL
libc = CDLL("libc.so.6") 
libc.srand(0x1337)
f=open('flag.enc','rb')
X=[]
while(True):
	c=f.read(1)
	if not c:
		break
	b = int.from_bytes(c, byteorder='big')
	M=hex(b^libc.rand()^libc.rand()).strip()[-2:]
	X.append(chr(int(M,16)))
print(''.join(X))
```

Flag:gigem{d0n7_wr173_y0ur_0wn_c1ph3r5}