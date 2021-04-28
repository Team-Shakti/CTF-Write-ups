# Awesome Encryption Scheme

Authored by: Sowmya (@__4lpha\_\_)

Challenge Script:
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import md5
from os import urandom
from flag import flag

keys = [md5(urandom(3)).digest() for _ in range(2)]


def bytexor(da,ta): return bytes(i^j for i,j in zip(da,ta))


def get_ciphers(iv1, iv2):
    return [
        AES.new(keys[0], mode=AES.MODE_CBC, iv=iv1),
        AES.new(keys[1], mode=AES.MODE_CFB, iv=iv2, segment_size=8*16),
    ]

def encrypt(m: bytes, iv1: bytes, iv2: bytes) -> bytes:
    m = pad(m,32)
    ciphers = get_ciphers(iv1, iv2)
    c = m
    for cipher in ciphers:
        c = b''.join(i[16:]+bytexor(i[:16],cipher.encrypt(i[16:])) for i in [c[i:i+32] for i in range(0,len(c),32)])
    return c

plaintext = f'finally now i am able to send my secret with double security and double trust, {flag}'.encode()
iv1, iv2 = urandom(16),urandom(16)

ciphertext = encrypt(plaintext, iv1, iv2)
ciphertext = b":".join([x.hex().encode() for x in [iv1, iv2, ciphertext]])

open('encrypted','wb').write(ciphertext)
```

Output:
```
c486732c526c5b60bc29bae6926644eb:5fe355033095d413e601a7ede00fca1d:fd68e8732bb6e9b5672730eb1ed3f2fe9c88b5503e3fb08747ce3dd17296e383ccb76b78587bb1bd1337574073a185e9d846aeab36929d0101e433a34db0cf9ed034abb473a2280624d430c39e58c245603f56a4ddb1127a9f74051481440bbbe53fd95bc8a2a9a3f3488c68d1d9fa8e82cb40dce3df7b2d1c22fca0d05d08c9d197e053586643b32d3dbd4421996ad6abf2a1a930eb16609303471808bac90b
```

This is a customised encryption scheme. So let's take a look at the block diagram to get better understanding of the encryption scheme.

Enryption Block Diagram:
```
                          Message-Block
        ----------------------------------------------------
        |        L0             |               R0         |
        ----------------------------------------------------
                  |                             |
                  |         -------------       |
                  V         |           |       |
                  ⊕ <-------|  AES-CBC  |<------|
                  |         |           |       |
                  |         -------------       |
                  |                             |
                  |                             |
                  -------------------------|    |
                                            \   |
                                             \  |
                  |---------------------------\--
                  |                            \
                  |                             |
                  V           Meet              V
        ----------------------------------------------------
        |        L1  ==  R0     |      L2  ==  R1          |
        ----------------------------------------------------
                  |                             |
                  |         -------------       |
                  V         |           |       |
                  ⊕ <-------|  AES-CFB  |<------|
                  |         |           |       |
                  |         -------------       |
                  |                             |
                  |                             |
                  -------------------------|    |
                                            \   |
                                             \  |
                  |---------------------------\--
                  |                            \
                  |                             |
                  V       Cipher-Block          V
        ----------------------------------------------------
        |        L2             |               R2         |
        ----------------------------------------------------
```
Observation:
If we notice the block diagram we can say that the encryption function is using two rounds of fiestal structure
* Now we have `L1||R1`
* Key is a hash of 3 random bytes (can be bruteforced)

We can find the key used for `AES-CBC` by using `L0, R0, R1(L2)`:
* Since `R1 = L0 ^ E( R0 ) `where `E` stands for `CBC-Encryption`
```
            -> R1 = L0 ^ E( R0 )
            -> R1 ^ L0 = E(R0)
            -> L2 ^ L0 = E(R0)
```
* Now we have a pair of `plaintext & ciphertext` pair which help in bruteforcing the CBC-key

In detail: 
```
keys        =   [ md5(bytes([i,j,k])).digest() for i in range(256) for j in range(256) for k in range(256) ]
key1      =   [ i for i in keys if bytexor(pt[:16],AES.new(i,AES.MODE_CBC,iv1).encrypt(pt[16:32])) == ct[:16] ][0]
```
We can find the key used for `AES-CFB` by using `L2, R2, L1(R0)`:
* Since `R2 = L1 ^ E( R1 ) `where `E` stands for `CBC-Encryption`
```
            -> R2 = L1 ^ E( R1 )
            -> R2 ^ L1 = E( R1 )
            -> R2 ^ R0 = E( L2 )
```
* Now we have a pair of `plaintext & ciphertext` pair which help in bruteforcing the CFB-key

In detail: 
```python
key2 = [ i for i in keys if bytexor(AES.new(i,AES.MODE_CFB, iv2,segment_size=8*16).encrypt(ct[:16]),ct[16:32]) == pt[16:32] ][0]
```

Now we have the both `key1` and `key2`, so we can reverse the encryption process to decrypt the ciphertext.
In detail: 
```python
def decrypt(c: bytes, iv1: bytes, iv2: bytes) -> bytes:
    ciphers = get_ciphers(iv1, iv2)
    m = c
    for cipher in ciphers[::-1]:
        m = b''.join(bytexor(i[16:],cipher.encrypt(i[:16]))+i[:16] for i in [m[i:i+32] for i in range(0,len(m),32)])
    return unpad(m,32)
```

Solution Script:
```python
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def bytexor(da,ta): return bytes(i^j for i,j in zip(da,ta))


def get_ciphers(iv1, iv2):
    return [
        AES.new(keys[0], mode=AES.MODE_CBC, iv=iv1),
        AES.new(keys[1], mode=AES.MODE_CFB, iv=iv2, segment_size=8*16),
    ]


def decrypt(c: bytes, iv1: bytes, iv2: bytes) -> bytes:
    ciphers = get_ciphers(iv1, iv2)
    m = c
    for cipher in ciphers[::-1]:
        m = b''.join(bytexor(i[16:],cipher.encrypt(i[:16]))+i[:16] for i in [m[i:i+32] for i in range(0,len(m),32)])
    return unpad(m,32)


(iv1, iv2, ct),pt = (bytes.fromhex(i) for i in open('encrypted','rb').read().strip().decode().split(':')), b'finally now i am able to send my secret with double security and double trust, '

keys        =   [ md5(bytes([i,j,k])).digest() for i in range(256) for j in range(256) for k in range(256) ]
key1      =   [ i for i in keys if bytexor(pt[:16],AES.new(i,AES.MODE_CBC,iv1).encrypt(pt[16:32])) == ct[:16] ][0]
key2    =   [ i for i in keys if bytexor(AES.new(i,AES.MODE_CFB, iv2,segment_size=8*16).encrypt(ct[:16]),ct[16:32]) == pt[16:32] ][0]

keys = [ key1, key2]

flag = decrypt(ct,iv1,iv2)[79:]
print(flag)
```

Flag: `shaktictf{Well now I know that it is not an awesome encryption scheme}`