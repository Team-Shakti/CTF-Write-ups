# REach The Moon

**Challenge author**[imm0rt4l_5t4rk](https://twitter.com/SimranKathpalia)

**Challenge points:** 200

**Challenge solves:** 6

### Challenge Description
Enter the correct flag to reach the moon. Your input will include shaktictf{} in it. Keep that in mind.

### Solution
In the challenge the program asks us to input two strings eac of which is of length 17. Using the two strings various operations are conducted using them and the result is stored in a check array. The check array is being compared to a string of length 20 which is `shaktictf{N0FL4GY3t?}`. If it passes the comparison it gives us the flag(which was our input itself). Otherwise if it fails it returns Not there yett. 

To solve such a challenge where we have to find a probable answer consisting of many equations and conditions
that are not solvable by hand or are time taking we generally use python tools such as z3-solver or angr.

Below is a z3 script to get one definite solution based on the conditions given in the challenge.

```python
from z3 import *

a1 = [
BitVec("a1[0]", 16),
BitVec("a1[1]", 16),
BitVec("a1[2]", 16),
BitVec("a1[3]", 16),
BitVec("a1[4]", 16),
BitVec("a1[5]", 16),
BitVec("a1[6]", 16),
BitVec("a1[7]", 16),
BitVec("a1[8]", 16),
BitVec("a1[9]", 16),
BitVec("a1[10]", 16),
BitVec("a1[11]", 16),
BitVec("a1[12]", 16),
BitVec("a1[13]", 16),
BitVec("a1[14]", 16),
BitVec("a1[15]", 16),
BitVec("a1[16]", 16)
]

a2 = [
BitVec("a2[0]", 16),
BitVec("a2[1]", 16),
BitVec("a2[2]", 16),
BitVec("a2[3]", 16),
BitVec("a2[4]", 16),
BitVec("a2[5]", 16),
BitVec("a2[6]", 16),
BitVec("a2[7]", 16),
BitVec("a2[8]", 16),
BitVec("a2[9]", 16),
BitVec("a2[10]", 16),
BitVec("a2[11]", 16),
BitVec("a2[12]", 16),
BitVec("a2[13]", 16),
BitVec("a2[14]", 16),
BitVec("a2[15]", 16),
BitVec("a2[16]", 16)
]

check = "shaktictf{0Fl4gY3t?}";
c = []
for i in range(len(check)):
	c.append(ord(check[i]))


s = Solver()

for i in range(17):
	s.add(a1[i]>40, a1[i]<127)
	s.add(a2[i]>40, a2[i]<127)
s.add(c[0] == a1[0]) #We have hardcoded the starting characters to be 'shaktictf{' and last character to be '}' because it says in the
s.add(c[1] == a1[1]) #description that the input will have the flag format in it.
s.add(c[2] == a1[2])
s.add(c[3] == a1[3])
s.add(c[4] == a1[4])
s.add(c[5] == a1[5])
s.add(c[6] == a1[6])
s.add(c[7] == a1[7])
s.add(c[8] == a1[8])
s.add(c[9] == a1[9])
s.add(c[19] == a2[16])
print(s.check())
s.add(c[0] == (a1[0] - 71) ^ a2[0])
s.add(c[1] == LShR(a1[1],2) + (a2[1] - 0x7))
print(s.check())
s.add(c[2] == (3 * (a2[2] - (a1[2] ^ 0x2d))) - 0x14)
s.add(c[3] == (2 * (a1[3] - a2[3])) ^ 0x1b) 
s.add(c[4] ==  (a1[4] + a2[4]) ^ 0xa7)
s.add(c[5] == a1[5] & (a2[5] + 0x6f)) 
s.add(c[6] == (a1[6] % a2[6]) + 0x33)
s.add(c[7] == (a1[7] ^ 0x61) + a2[7])
s.add(c[8] == (~a1[8] + 0xbd) ^ a2[8])
s.add(c[9] == (a2[9] ^ 0x30) + (a1[9] ^ 0x42)) 
s.add(c[19] == (LShR(a1[16], 0x2) + (a2[16] ^ 0x1d)))
s.add(a2[0] == a2[10])
s.add(c[10] == LShR(a2[11], a1[11] / 0x1f))
s.add(c[11] == (a2[3] - a1[11]) * 0x23)
s.add(c[12] == a2[12] ^ a1[12] ^ 0x46)
s.add(c[13] == (~a2[13] % 0x100) - a1[12])
s.add(c[14] == a2[13])
s.add(c[15] == LShR(a2[14],0xc1) - (~a1[13] ^ 0x7))
s.add(c[16] == (a1[14] % 0x7a) + (a2[14] % 0x73) - 0xb8) 
s.add(c[17] == (a2[14] % 0x73) + (~a1[15] + 0x33))
s.add(c[18] == a1[16] % 118 & a2[15] ^ 10)
l = ((a2[0] ^ 4) ^ 31)
s.add(a1[10] == l)
s.add(a1[10] == a2[15] + 5)
s.add(a2[15] == 63)


print(s.check())
#print(s.model())
m = s.model()
w = ''
x = ''
for i in range(17):
    w += chr(m[a1[i]].as_long())
    x += chr(m[a2[i]].as_long())
print(w)
print(x)
```
Thus our two inputs become `shaktictf{D1d_y0u` and `_Us3_z3_0r_aNgr?}`

### Flag
shaktictf{D1d_y0u_Us3_z3_0r_aNgr?}
