# RedPWN CTF
## Challenge name:baby
### Description 
>> Given a "output.txt" file with n,e value 
Step-1: Get p,q values from n
>> Use sagemath for this
>> ![image](https://i.imgur.com/dAsfZ1N.png)
>> 
>> Use Crypto modules and gmpy2 for inverse
>> 
>> Requried equations :
  >>> n =p* q (p,q are primes)
  >>> 
  >>> d = inverse(e,phi(n))
  >>> 
  >>> pt = pow(ct,d,n)
```py
from Crypto.Util.number import * 
from Crypto.PublicKey import RSA 
import gmpy2                     

n= 228430203128652625114739053365339856393 
e= 65537 
c= 126721104148692049427127809839057445790  
#factor(n)        #in sage 
#12546190522253739887 * 18207136478875858439                      
p = 12546190522253739887   
q = 18207136478875858439 
phi = (p-1)*(q-1)          
d = inverse(e,phi)  
pt = pow(ct,d,n) 
print(long_to_bytes(pt))
```
``Flag ~  flag{68ab82df34}``
