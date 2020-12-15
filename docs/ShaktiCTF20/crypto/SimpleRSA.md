# SimpleRSA

### Challenge Description
Here's the secret message from Joan to you. Break it and Read it.

### Short writeup
Factordb helps in breaking the modulus. Online tools or code can be written to do RSA decryption.

```python

from Crypto.Util.number import *


# Use an online tool to factorise n. eg: factordb.com
p = 724804277
q = 9413710946631053481929229233058876904137902588796220199578081215560027062585806165966619995720300336586922201502376869335302844207978432570013597781850093
#n == p*q
c = 484661494807973176484841550022162356056969394230726278907827156279573785417739620605749085238379352332325669223692676583758711843467179784519220209212809010990483
e = 65537

d = inverse(e,(p-1)*(q-1))

m = pow(c,d,p*q)

print(long_to_bytes(m))
```
### Challenge Author

[4lph4](https://twitter.com/__4lph4__)

### Flag
shaktictf{Gr3a7-g01ng-g1rl-Y4yyy!!}
