# Wii Phit

Solved by: Sowmya (@__4lph4\_\_)

This was an interesting challenge from Cyber Apocalypse CTF 2021. This challenge is based on Number Theory and I really liked the way this challenge was created.

Here's the challenge script for understanding the challenge: 

```python
from Crypto.Util.number import bytes_to_long
from secrets import FLAG,p,q

N = p**3 * q
e = 0x10001
c = pow(bytes_to_long(FLAG),e,N)

print(f'Flag: {hex(c)}')

# Hint

w = 25965460884749769384351428855708318685345170011800821829011862918688758545847199832834284337871947234627057905530743956554688825819477516944610078633662855
x = p + 1328
y = p + 1329
z = q - 1

assert w*(x*z + y*z - x*y) == 4*x*y*z
```


Parameter given to us:
```
Flag: 0x12f47f77c4b5a72a0d14a066fedc80ba6064058c900a798f1658de60f13e1d8f21106654c4aac740fd5e2d7cf62f0d3284c2686d2aac261e35576df989185fee449c20efa171ff3d168a04bce84e51af255383a59ed42583e93481cbfb24fddda16e0a767bff622a4753e1a5df248af14c9ad50f842be47ebb930604becfd4af04d21c0b2248a16cdee16a04b4a12ac7e2161cb63e2d86999a1a8ed2a8faeb4f4986c2a3fbd5916effb1d9f3f04e330fdd8179ea6952b14f758d385c4bc9c5ae30f516c17b23c7c6b9dbe40e16e90d8734baeb69fed12149174b22add6b96750e4416ca7addf70bcec9210b967991e487a4542899dde3abf3a91bbbaeffae67831c46c2238e6e5f4d8004543247fae7ff25bbb01a1ab3196d8a9cfd693096aabec46c2095f2a82a408f688bbedddc407b328d4ea5394348285f48afeaafacc333cff3822e791b9940121b73f4e31c93c6b72ba3ede7bba87419b154dc6099ec95f56ed74fb5c55d9d8b3b8c0fc7de99f344beb118ac3d4333eb692710eaa7fd22
```

Getting into my initial approach, I first tried elaborating this: `assert w*(x*z + y*z - x*y) == 4*x*y*z` thinking that it would give me a relation in one of the primes of the modulus. But that didn't work out. 

On staring at the equation for sometime, I found it similar to one the maths algebra kind of relation. Rearranging the equation gave me this equation: 
`4/w = 1/x + 1/y - 1/z`

I searched for similar equations on the internet and I luckily found [this](https://scialert.net/fulltext/?doi=aja.2011.31.37#:~:text=The%20above%20relation%20can%20also,this%20is%20a%20Diophantine%20equation)

According to the above link
w = n
x = (n-1)/2
y = (n+1)/2
z = n(n-1)(n+1)/4

Once we get x,y,z we can simply get the prime factors `p,q` with which we can construct Modulus `N` and `phi(n)` to solve the RSA problem. 

Solution script:
```
from Crypto.Util.number import *
w = 25965460884749769384351428855708318685345170011800821829011862918688758545847199832834284337871947234627057905530743956554688825819477516944610078633662855
flag = 0x12f47f77c4b5a72a0d14a066fedc80ba6064058c900a798f1658de60f13e1d8f21106654c4aac740fd5e2d7cf62f0d3284c2686d2aac261e35576df989185fee449c20efa171ff3d168a04bce84e51af255383a59ed42583e93481cbfb24fddda16e0a767bff622a4753e1a5df248af14c9ad50f842be47ebb930604becfd4af04d21c0b2248a16cdee16a04b4a12ac7e2161cb63e2d86999a1a8ed2a8faeb4f4986c2a3fbd5916effb1d9f3f04e330fdd8179ea6952b14f758d385c4bc9c5ae30f516c17b23c7c6b9dbe40e16e90d8734baeb69fed12149174b22add6b96750e4416ca7addf70bcec9210b967991e487a4542899dde3abf3a91bbbaeffae67831c46c2238e6e5f4d8004543247fae7ff25bbb01a1ab3196d8a9cfd693096aabec46c2095f2a82a408f688bbedddc407b328d4ea5394348285f48afeaafacc333cff3822e791b9940121b73f4e31c93c6b72ba3ede7bba87419b154dc6099ec95f56ed74fb5c55d9d8b3b8c0fc7de99f344beb118ac3d4333eb692710eaa7fd22
x = (w-1)//2
y = (w+1)//2
z = w*x*y
p = x - 1328
q = z + 1
N = p**3 * q
e = 65537
phin = (p-1)*(p**2)*(q-1)
d = inverse(e,phin)
flag = long_to_bytes(pow(flag,d,N))
print(flag)
```

On running the script, we get the flag: `CHTB{Erdos-Straus-Conjecture}`

