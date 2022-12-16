
## cAex0r
### Challenge Description :
I tried to develop a new generator but I am not sure how it is working. 
### Difficulty Level
Easy

### Author
[b4b7gr00t](https://twitter.com/Paavani21)

### Points
100

### Flag format 
shaktictf{...}

### Writeup

This challenge is the combination of Ceaser cipher and xor. The number of letters to be shifted is given as a random number, and the key is also a random string with lenght `3` for xor.

The idea is to use a `Known Plaintext attack`.
 You have cass function, which does Ceaser cipher encryption and ciphertext.
Use the flag format `shaktictf{`.
 Brute for the `stride` value within the range of 1 to 27.
 xor `cass(b'sha',brute value)` and `ct[:3]` to get the key. xor that key with ciphertext. check whether `shaktictf{` is in `cass(pt,brute value)`.
 
```python=
from itertools import product
from pwn import xor
ct = open("ciphertext.txt","rb").read()

def cass (text,stride):
    u_alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_alpha="abcdefghijklmnopqrstuvwxyz"
    enc_text = ""
    for i in text:
        if i>=65 and i<= 90:
            enc_text += u_alpha[(u_alpha.find(chr(i)) + stride)%26]
        elif i>=97 and i<= 122:
            enc_text += l_alpha[(l_alpha.find(chr(i)) + stride)%26]
        else:
            enc_text += chr(i)
    return enc_text.encode()



for i in range(1,27):
    key = xor(cass(b'sha', i),ct[:3])
    pt = xor(ct,key)
    if b'shaktictf{' in cass(pt,-i):
        print(cass(pt,-i).decode())


```


#### Flag 
`shaktictf{welCom3_t0_cRyptOo_WoRLD_77846b12bfd9b91ebce67b236aa4}`



