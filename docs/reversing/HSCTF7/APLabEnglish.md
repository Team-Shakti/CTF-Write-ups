
# APLab:English


## Description

Another java Reversing Challenge. We are given a java file which is to be reversed.

## Solution


```
s="1dd3|y_3tttb5g\`q]^dhn3j"
def unxor(string):
    ret=''
    xorstr=[4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3]
    for i in range(len(string)):
        ret+=chr(ord(string[i])^xorstr[i])
    return ret




def untranspose(string):
    ret=[None]\*23
    transpose=[11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9]
    for i in range(len(transpose)):
        ret[transpose[i]]=string[i]
    return ''.join(ret)


for i in range(3):
    s=unxor(s)
    print(s)
    s=untranspose(s)
    print(s)
```

### Output

`
5eg2~x\3upwc7gau\\gjo3i
cj3o\\pg~i35uaug\xe2gw7
gk0n^]sgm04watc]zf0fw4
40gf]sma^4wgtc0z]knf0w
01dg_rna_0tf}tb4{_hlg0t
flag{n0t_t00_b4d_r1ght}
`
