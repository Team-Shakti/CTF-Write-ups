
# Dis HSCTF2020

## Description

The challenge was a python bytecode challenge where the approach I chose was to maually replicate the bytecode from the documentation of the dis module in python which took up a while. Im not sure if there's a less time consuming approach but once that was done the reversing part was automated using Z3.

## Solution

'''python

bytestring=b'\xae\xc0\xa1\xab\xef\x15\xd8\xca\x18\xc6\xab\x17\x93\xa8\x11\xd7\x18\x15\xd7\x17\xbd\x9a\xc0\xe9\x93\x11\xa7\x04\xa1\x1c\x1c\xed'
from z3 import *


def a(s):
    o = [0] * 32
    for i in range(32):
        o[i] = ((s[i]+s[i])-60)
    return o
def b(s,t):
    for x,y in zip(s,t):
        yield(x+y)-50
def c(s):
    return [x+5 for x in s]

def e(s):
    s = [ i for i in s ]
    o = [ (o^5)-30 for o in b(a(s),c(s)) ]
    return o

def main():
    sol=Solver()
    o=b'\xae\xc0\xa1\xab\xef\x15\xd8\xca\x18\xc6\xab\x17\x93\xa8\x11\xd7\x18\x15\xd7\x17\xbd\x9a\xc0\xe9\x93\x11\xa7\x04\xa1\x1c\x1c\xed'
    l=list(o)
    s = [ BitVec('s[%s]' % i, 8) for i in range(32) ]
    s = e(s)
    for i in range(len(l)):
        sol.add(s[i]==l[i])
    print(sol.check())
    print(sol.model())
main()



<p align="center">

<img src = "../../images/dis.png" width="200" height="200" >

</p>

` Flag: flag{5tr4ng3_d1s45s3mbly_1c0a88}`
