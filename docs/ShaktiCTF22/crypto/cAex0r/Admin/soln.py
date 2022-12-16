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


