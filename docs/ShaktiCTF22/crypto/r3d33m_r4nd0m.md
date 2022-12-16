
### r33d3m_rand0m

### Challenge Description :
You know, everything is fair in CTFs and competition.

### Author
[b4b7gr00t](https://twitter.com/Paavani21)

### Difficulty Level
Hard

### Points
300

### Flag format 
shaktictf{...}

#### Writeup

This is a simple `Random faults attack` which works with RSA decryption and signature verification with CRT. A signature can be built using CRTof Sp, Sq, Sr. Sp, Sq, and Sr are signatures of hash function with p,q, and r, respectively. 

```py=
p,q,r = getPrime(256),getPrime(256),getPrime(256)
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

```

`s` is the signature.

Now, it is easy to find p,q,r,when the attacker has the full knowledge of `h`.


If the signature is valid, i.e., `s^e mod N = h`, the attacker has a chance to manipulate `Sp, Sq and Sr` values. If you compute the signature using changed `Sp, Sq, and Sr` values, the verification fails. Now give faults Sp value, i.e., add some value to `Sp ( Sp+3 )` for first signature verification and don’t change `Sq and Sr`. Calculate `gcd(S^e - h,n)`, which is equal to the `product of q and r`. In the same way, input `Sp, modified_Sq, Sr`, and get the `product of p and r`. Next, find the `product of p and q`.


```python=
sp1 = sp+2      #create faults value one each time
sq1 = sq+2      #create faults value
sr1 = sr+2


io = remote(host,port)    
io.recvuntil(b'provided\n')
n = int(io.recvline()[4:-1])
e = int(io.recvline()[4:-1])
h = int(io.recvline()[4:-1])
io.recvuntil(b'values\n')
io.sendline('2')
io.recvuntil(b'sp value: ')
io.sendline(str(sp1))
io.recvuntil(b'sq value: ')
io.sendline(str(sq))
io.recvuntil(b'sr value: ')
io.sendline(str(sr))

qr = GCD((s**e)-h , n )
```

```python=
pr = GCD((s**e)-h , n)
pq = GCD((s**e)-h , n)

p = GCD(pq,pr)
q = GCD(pq,qr)
r = GCD(pr,qr)     
```

find `pq` and `pr` in the same way. 

Now find the `gcd(pq,pr),gcd(pq,qr) and gcd(pr,qr)` to get `p`,`q` and `r` values respectively.

```python=
phi = (p-1)*(q-1)*(r-1)
d = inverse(e,phi)
pt = long_to_bytes(pow(ct,d,n))

print(pt)

```

#### flag

`shaktictf{rand0m_cr4z7_p3rs0n_aLw4ys_tries_cr7pt0_a7de4873ca0f9f697f1d2c09004f33dc1ad98b64}`
