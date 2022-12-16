from secret import flag
from random import randint
from pwn import xor
from os import urandom
stride = randint(1,27)
s1 = flag[:len(flag)//2]
s2 = flag[len(flag)//2:]
key = urandom(3)

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

c = xor(cass(s1+s2,stride),key)
x = open("ciphertext.txt", "wb") 
x.write((c))

