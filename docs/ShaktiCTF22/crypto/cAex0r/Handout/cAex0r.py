from secret import flag,key
from random import randint

stride = randint(1,27)
s1 = flag[:len(flag)//2]
s2 = flag[len(flag)//2:]
assert(len(key) == 1)

def cass (text,stride):
    u_alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_alpha="abcdefghijklmnopqrstuvwxyz"
    enc_text = ""
    for i in text:
        if i>=65 and i<= 90:
            enc_text += u_alpha[(u_alpha.find(chr(i)) - stride)%26]
        elif i>=97 and i<= 122:
            enc_text += l_alpha[(l_alpha.find(chr(i)) - stride)%26]
        else:
            enc_text += chr(i)
    return enc_text.encode()

def xorr(text, key):  
     return bytes([b ^ ord(key) for b in text])  

c1 = xorr(cass(s1,stride),key)
c2 = xorr(cass(s2,stride),key)
x = open("../../cAex0r/ciphertext.txt", "w") 
x.write((c1 + b"@@" + c2).decode())
x.close()
