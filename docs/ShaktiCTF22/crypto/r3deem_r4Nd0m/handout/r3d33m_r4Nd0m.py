from hashlib import sha256
from Crypto.Util.number import *
from secret import p,q,r,flag


# p,q,r = getPrime(256),getPrime(256),getPrime(256)
n =  p*q*r
e = 65537
phi = (p-1)*(q-1)*(r-1)
d = inverse(e,phi)
ct = pow(bytes_to_long(flag),e,n)

h =int(sha256(flag).hexdigest(),16)

dp = d%(p-1)
dq = d%(q-1)
dr = d%(r-1)

sp = pow(h,dp,p)
sq = pow(h,dq,q)
sr = pow(h,dr,r)

s = (((sp*q*r*(inverse(q*r,p)))%n) + (sq*p*r*(inverse(p*r,q)) %(n)) + ((sr*p*q*(inverse((p*q),r)))%n))%n 




    
