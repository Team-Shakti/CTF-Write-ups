## Eat Sleep Trace Repeat

Script:

```python
def func1(a):
    o = ""
    # & 0xffffffffffffffff is used to convert integer to 64 bit(8 bytes)
    b = (((a >> 0xc) & 0xffffffffffffffff) ^ a) & 0xffffffffffffffff
    c = (((b << 0x19) & 0xffffffffffffffff) ^ b) & 0xffffffffffffffff
    d = (((c >> 0x1b) & 0xffffffffffffffff) ^ c) & 0xffffffffffffffff
    out = d * 0x2545f4914f6cdd1d
    out = out & 0xffffffffffffffff
    arr.append(chr(out & 0xff))
    return d

arr = []
inp = 0x41424344
for i in range(0x800):
    inp = func1(inp)
    inp = inp & 0xffffffffffffffff

chall_file = open('trace.txt', 'r')
lines = chall_file.readlines()
l1 = []
for line in lines:
    l1.append(line.split(' : ')[0])

index = []
cnt = 0
for i in l1:
    if (i == "0x401122"):
        cnt = cnt + 1
    if(i == "0x401130"):
        index.append(cnt)
        cnt = 0

flag = ""
for i in index:
    flag = flag + arr[i-1]

print(flag)
```

**Flag:** zh3r0{d1d_y0u_enjoyed_r3v3rs1ng_w1th0ut_b1n4ry_?}