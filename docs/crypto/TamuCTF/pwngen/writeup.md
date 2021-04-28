# TamuCTF

## pwngen

*Challenge points* : 150
*Challenge solves* : 10

### Description

(*not the exact description*)

It has been found that a set of passwords have been generated using the given script.We have reason to believe that they generated a set of passwords at the same time using a custom password generation program and that their previous password was `ElxFr9)F`. Send the next password at `openssl s_client -connect tamuctf.com:443 -servername pwgen -quiet`.

Files : [main.rs]()

## Writeup

Author : [ph03n1x](https://github.com/meenakshisl)

**TL;DR**
1. Given the equation of a Linear congruential generator (LCG) and the previous password generated using it
2. Use z3 to find the seed with the given contraints.
3. Find the seed and get the next password from it.

## Solution

On inspecting the file we understand that it is a LCG generator. We decided to give it a try with z3 python, so we decided to rewrite the functions in python (becuase we were more familiar with python than rust):-

```python

class LCG() : 
    def __init__(self,seed) : 
        self.seed = seed 
        self.a = 1103515245 
        self.c = 12345 
    def next(self) : 
        self.seed = ((self.seed * self.a) + self.c)%0x100000000 
        out = (self.seed >> 16) & 0x7fff 
        return out
def get_pass(rand) : 
    l = [] 
    for i in range(8) : 
        l.append(chr(rand.next()%94 + 33)) 
    return ''.join(l) 
```

The code should produce the same output as the given rs file. Now we simply used z3 to setup the contraints and find the seed :-

```python
from z3 import *

known = 'ElxFr9)F' 

class LCG() :
    def __init__(self,seed) :
        self.seed = seed
        self.a = 1103515245
        self.c = 12345
    def next(self) :
        self.seed = ((self.seed * self.a) + self.c)%0x100000000
        out = (self.seed >> 16) & 0x7fff
        return out
def get_pass(rand) :
    return URem(rand.next(),94) + 33

s = Solver()
seed = BitVec("seed",32)
l = LCG(seed)
for i in known :
    s.add(get_pass(l) == ord(i))
s.check()
seed = s.model()[seed]
```

We get our seed as `seed = 718549711`. 
(*Note* : Make sure you use modify the class to the inital class definition since the second one has been slightly modified to take in z3 objects)
Now let's predict the password :-

```python
seed = 718549711      
l = LCG(seed)         
print(get_pass(l) )          
# output : 'ElxFr9)F'
get_pass(l)           
# output 'xV!;28vj'
```

Now to connect to the server and send the password :-

![get_flag](https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/TamuCTF/pwngen/get_flag.png)

**Flag** : `gigem{cryp706r4ph1c4lly_1n53cur3_prn65_DC6F9B}`