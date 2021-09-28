# MultipleExponents - Crypto
### Sloved by - [pavani](https://github.com/Paavani-git)
### Description
```
Both Alice and Bob share the same modulus, but with different exponents. If only there was some way I could recover this message that was sent to both of them.

Author: Ratman#4736
```
### Writeup
~Attack:Common modules~
We have one modulus, two exponents and two ciphertexts 

Equations:
```
gcd(e1,e2) = 1 => e1 * u +e2 * v = 1  ---->1
C1 = M^{e_1} mod n , C2 = M^{e_2} mod n
M^{e_1*u}*M^{e_2*v} = M^{e_1*u+e_2*v} = M^1 = M  --->2

```
Now use Extended Euclid Algorithm on equation1 to get u,v; Use ``xgcd`` in sagemath to get u,v respectively
If u < 0 , find inverse of C1 mod n .If v<0 ,then find the inverse of C2 mod n
As I got u < 0, I found inverse of C1.Now, according to equation-3 compute  M = c_1^u*c_2_{inv}^{-v}

### Script

### Flag
`` sun{d0n7_d0_m0r3_th4n_0ne_3xp0n3nt}``
