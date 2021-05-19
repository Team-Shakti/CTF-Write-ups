# dCTF 
## Strong password
![shakti](https://github.com/aryaarun12/CTF-Write-ups/blob/master/docs/crypto/dCTF/asset/spwd.png?raw=true)
- Given is a password protected zip file
- On using the tool ```JohnTheRipper```, we find the password=```Bo38AkRcE600X8DbK3600```
- Opening the zip file, we find a lorem_ipsum text
- ```$ strings lorem_ipsum.txt | grep dctf``` gives the flag:
```
dctf{r0cKyoU_f0r_tHe_w1n}
```