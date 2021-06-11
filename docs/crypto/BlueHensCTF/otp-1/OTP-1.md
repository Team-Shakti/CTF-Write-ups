# OTP-1

## Description

Sloved By: Pavani (@Paavani15793872)

Here we have an intersting challenge which involves brute forcing.

![otp1](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/otp-1.png)

In the given file, code is given in php

![ciphertext](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/Selection_014.png)

Here we have two cipher texts, which are separated by @@

from this we can tell that all characters are uppercase letters. 

![sel14](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/Selection_014.png)


![sel15](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/Selection_015.png)

>> repeated xor :

![sel16](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/Selection_016.png)

Here we have two cipher texts, try to built a code which allows uppercase letters and xor cipher texts and flag. till now we know that the flag = "UDCTF{" (with length = 6)
Try to guess letters one by one and xor it with cipher texts accordingly.

![sel18](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/Selection_018.png)

![sel20](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/Selection_020.png)

![flag](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/crypto/BlueHensCTF/asset/flag(otp).png)

**Flag** : `UDCTF{w3lcome_t0_0ur_ctf}`




