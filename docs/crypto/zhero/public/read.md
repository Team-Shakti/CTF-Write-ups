
# Alice_bob_dave - Crypto

#### Sloved by - Sowmya (@__4lph4\_\_) , Pavani(@PavaniPoluru)

## Description
   ```
   Alice and Bob are sending their flags to Dave. But sadly Dave lost the modulus :( Try to retrive the flag!
   ```
   This is a intresting RSA challenge. where we have to find modulous (n) from ct,d,e.
   I used sage to find n_a and n_b.
## RSA equations known
```d ≡ e^1 mod phin(n)
   d*e ≡ 1 mod phin(n)
   => d*e = k*phin(n)+1
   => da*e-1 = k(p-1)*(q-1)
   pt = long_to_bytes(pow(ct,d,n))
   ct = long_to_bytes(pow(pt,e,n))
```
``d*e = k*phin(n)+1``
From this try to find phin_a,phin_b 
  ``phi(n = (p-1)*(q-1)``
  ```phin_a = (d_a * e)-1
     phin_b = (d_b * e) -1
  ```
  
  
  we can find factors of p and brutefroce it with conditions is_prime and size(1024)
   
   ```
   sage: for i in range(1,10000): 
....:     p = ((GCD(phin_a,phin_b) // i) + 1) 
....:     if (is_prime(p) == 1) and (size(p) == 1024): 
....:         print(p) 
....:         print(i) 
....:         print(size(p)) 
....:                                                  
   ```
  
  find q,r in the same way
  `` p=177279130816191665059944783286411855023035031289227941571673915784074353287733189099688126318264113305321082059619767094038966996649561164342515779196140056547333435193040798074799909334916510316728847254833619137382153503950749154356946058670079132324988450725735937306884337410304401871741381990982764516163
  ``
    
  Now we know p
  >> n_a = p * q 
 
  >> n_b = p * r

```pt_a = long_to_bytes(pow(ct_a,d_a,p))
   pt_b = long_to_bytes(pow(ct_b,d_b,p))
```
  
Using this above equation find pt_a and pt_b
we can get pt_a + pt_b as:
```
b'Hey Dave its Alice here.My flag is zh3r0{GCD_c0m3s_'
b'Hey Dave its Bob here.My flag is 70_R3sCue_3742986}'
```
#### FLAG - zh3r0{GCD_c0m3s_70_R3sCue_3742986}
