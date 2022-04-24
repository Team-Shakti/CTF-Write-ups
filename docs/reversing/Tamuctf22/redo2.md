# redo2
## Description
Honestly, this is just a plain an simple ASM challenge. Best of luck.

## Solution
Here, we are given an assembly file which is in intel format, so we first convert it into intel by adding a statement in the assembly file - ".intel_syntax noprefix"
After this we compile the file - "gcc -m32 redo2.S -o redo2"

Observe the binary in binary ninja

### Script

```
flag=[]
"""
flag[0]=0x36
flag[1]=0x38
flag[2]=0x36
flag[3]=0x34
flag[4]=0x3c
flag[5]=0x4a
flag[6]=0x30
flag[7]=0x30
flag[8]=0x30
flag[9]=0x2e
flag[10]=0x31
flag[11]=0x31
flag[12]=0x31
flag[13]=0x31
flag[14]=0x2e
flag[15]=0x32
flag[16]=0x32
flag[17]=0x32
flag[18]=0x32
flag[19]=0x32
flag[20]=0x2e
flag[21]=flag[15]+1
flag[22]=0x2e
flag[23]=3
flag[24]=4
flag[25]=0
flag[26]=2
flag[27]=1
flag[28]=flag[5]+0x2
"""
flag.append(0x36)
flag.append(0x38)
flag.append(0x36)
flag.append(0x34)
flag.append(0x3c)
flag.append(0x4a)
flag.append(0x30)
flag.append(0x30)
flag.append(0x30)
flag.append(0x2e)
flag.append(0x31)
flag.append(0x31)
flag.append(0x31)
flag.append(0x31)
flag.append(0x2e)
flag.append(0x32)
flag.append(0x32)
flag.append(0x32)
flag.append(0x32)
flag.append(0x32)
flag.append(0x2e)
flag.append(0x32+0x1)
flag.append(0x2e)
flag.append(3)
flag.append(4)
flag.append(0)
flag.append(2)
flag.append(1)
flag.append(0x4a+0x2)

gg=[]
for i in flag:
    g=0
    g=i+0x31
    gg.append(chr(g))
fl=''
fl=''.join(gg)
print(fl)
```

We get our flag as the output 
```
gigem{aaa_bbbb_ccccc_d_45132}
```
