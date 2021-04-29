## setecAstronomy

Reverse the operations given.

```python
def xx(a, b):
    l=[]
    for i in range(len(a)):
        l.append(str(int(a[i])^int(b[i])))
    return l

out = "11001010011011101100110001011000111110101010111000001100011101101111100001111010001000100110000011100100100110001110000001111101"
phoenix = list(out)
ph = phoenix[::-1]
abbott = ph[0:32]
cosmo = ph[32:64]
ayk0 = ph[64:96]
earl = ph[96:128]

ayk64 = xx(earl,ayk0)
ayk96 = xx(cosmo,ayk64)
ayk32 = xx(abbott,ayk96)

ayk = ayk0 + ayk32 + ayk64 + ayk96

ayk[95:99], ayk[81:85] = ayk[81:85], ayk[95:99]
ayk[63:71], ayk[120:128] = ayk[120:128], ayk[63:71]
ayk[54:62], ayk[32:40] = ayk[32:40], ayk[54:62]
ayk[3:7], ayk[19:23] = ayk[19:23], ayk[3:7]

in0 = ayk[0:32]
dave = ayk[32:64]
red = ayk[64:96]
king = ayk[96:128]

in96 = xx(red, in0)
in64 = xx(dave, in96)
in32 = xx(king, in64)

final = in0 + in32 + in64 + in96
print("".join(final))
```

Output string: 01110100001100000110111101011111010011010011010001101110010110010101111101110011001100110110001101010010001100110111010001010011

Decoding it gives `t0o_M4nY_s3cR3tS`

**Flag:** gigem{t0o_M4nY_s3cR3tS}