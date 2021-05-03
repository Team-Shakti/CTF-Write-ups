# OTP-1

## Description

Sloved By: Pavani (@Paavani15793872)

Here we have an intersting challenge which involves brute forcing.

![otp1](../../asset/otp-1.png)

[OTP-1 FILE](https://bluehens.ctfd.io/files/bcd960c240bc8ccd7ccf46d0c85095e4/otp1.php?token=eyJ1c2VyX2lkIjoyODMsInRlYW1faWQiOjIwMiwiZmlsZV9pZCI6Mzd9.YGG65Q.0NwTirE69YCv7yyLSx-X-1t3Iyo)

In the given file, code is given in php

![ciphertext](../../asset/ciphertext.png)

Here we have two cipher texts, which are separated by @@

from this we can tell that all characters are uppercase letters. 

![sel14](../../asset/Selection_014.png)


![sel15](../../asset/Selection_015.png)

repeated xor :

![sel16](../../asset/Selection_016.png)

Here we have two cipher texts, try to built a code which allows uppercase letters and xor cipher texts and flag. till now we know that the flag = "UDCTF{" (with length = 6)
Try to guess letters one by one and xor it with cipher texts accordingly.

![sel18](../../asset/Selection_018.png)

![sel20](../../asset/Selection_020.png)

![flag](../../asset/flag(otp).png)

##Flag
* UDCTF{w3lcome_t0_0ur_ctf}




