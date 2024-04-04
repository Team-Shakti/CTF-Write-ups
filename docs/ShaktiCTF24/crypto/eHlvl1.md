# eHlvl1
**Challenge Description :**

John, an ordinary office worker, receives a mysterious email filled with seemingly random numbers, letters and codes. Little does he know, it holds the key to uncovering a hidden treasure left behind by his eccentric uncle who loved ciphers and encryptions. To claim his unexpected inheritance, John must decipher the cryptic message using his newfound skills in cryptography.

**source.py**
```python=
from Crypto.Util.number import*
from gmpy2 import *
from secret import e,b,hint,msg,d
p = getPrime(512)
q = getPrime(512)
n = p*q
m = bytes_to_long(msg)
h = bytes([i^b for i in hint])
print(f"h = {hex(bytes_to_long(h))}")
ct = pow(m,e,n)
de = pow(ct,d,n)
assert(m == de)
print("ct = ",ct)
print("p = ",p)
print("q = ",q)
```
**output.txt**
```
h = 0x6f535e1b5e1b061b0c020f0b0b10134f535e1b4852555c575e1b59424f5e1b4f535a4f1b4c5a481b4354495e5f121b0112
ct =  90411409551177819360717236462351545237822367597930505531741437834918499125195272674859389978951589180632146502190429979348445123366914000167832349866368754227474060832624537550600921894849466284315037863094795265822884392628050584343158613338754532642964368052098136565157343201877382609610774291396944124354
p =  10425866553433272288676977376976736493869099145622614885498170561565122111495807572631609087909399078701783905493563029715011322065331636751277834978526061
q =  9215753518399683669080201592666232851634627861957009698720674021492716071355990364002777325458055207969176695525292834842774295594232711456066623178861093

```

**Author** : [im._.a.p](https://twitter.com/im_a_p_)

**Solution**:

* Values of 'p','q','ciphertext','h'(encrypted hint which has the value of e) is given.
* Th value of the modulus can be found using 'p' and 'q' as p*q = n.
* From the given code, we understand that 'hint' is xored with a random byte 'b' to get the ciphertext h.
* To find 'hint', 'h' is xored with each single byte (bruteforced) to get 'hint', thus getting the value of e.
```python=
from string import printable
h= '6f535e1b5e1b061b0c020f0b0b10134f535e1b4852555c575e1b59424f5e1b4f535a4f1b4c5a481b4354495e5f121b0112'
m= bytes.fromhex(h)
for i in range(256):
  x=bytes(i^j for j in m)
  try:

    x = x.decode()
    for j in x:
      assert j in printable
    print(i,x)
  except:
    pass
  
#59 The e = 79400+(the single byte that was xored) :)
#e = 79459
```
* With the values 'e','n','p','q', the ciphertext ct can be decrypted to get the message.
```python=
e = 79459
n = p*q
phi = (p-1)*(q-1)
d = invert(e,phi)
print(d)
hint = pow(ct,d,n)
print(long_to_bytes(hint))

#b"Here is your reward 'vvrkxuqgi{r0i43m0r_f0_hu3_u3gtu3!!!}' You can ask 'Doraemon' to help you with this. Bye!!"
#vinegere cipher key : doraemon
```
* The message has the encrypted flag and key which is to be decrypted.(vinegere cipher).

**Flag** : shaktictf{d0r43m0n_t0_th3_r3scu3!!!}
