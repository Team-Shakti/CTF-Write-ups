## CircleConCTF 21'

## CRT RSA

*Challenge Points : 100 Points*
*Solved by : 

### Writeup

**TL;DR**
- Hastard's Broadcast Attack

**Script**

```python
from sage.all import *
from Crypto.Util.number import long_to_bytes
eval(open("crt_rsa").read())
c = [ct_1,ct_2,ct_3]
n = [n_1,n_2,n_3]

print(long_to_bytes(gmpy.root(CRT(c,n),3)[0]))

```

#### Flag
`flag{infi_nite_jes_t}`