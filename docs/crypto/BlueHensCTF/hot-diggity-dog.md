# BlueHens CTF 
## Hot-diggity-dog 
![shakti](https://github.com/aryaarun12/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/hdd.png?raw=true)

[hot-diggity-dog.py](https://github.com/aryaarun12/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/hdd.py) 

[output.txt](https://github.com/aryaarun12/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/hdd.txt) 

- On observing the files, we find that it is a cryptographic attack- 'Wiener's attack'
- And we found a [script](https://github.com/MxRy/rsa-attacks/blob/master/wiener-attack.py) online to decrpyt it.
- Substituting our values and running it, directly gives us the flag..
```
UDCTF{5t1ck_t0_65537}
```
