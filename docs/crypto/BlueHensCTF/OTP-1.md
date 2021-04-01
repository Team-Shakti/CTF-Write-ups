# OTP-1

## Description

Sloved By: Pavani (@Paavani15793872)

Here we have an intersting challenge which involves brute forcing.

<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/otp-1.png" width = "300" height = "300" >

</p>

OTP-1 FILE (https://bluehens.ctfd.io/files/bcd960c240bc8ccd7ccf46d0c85095e4/otp1.php?token=eyJ1c2VyX2lkIjoyODMsInRlYW1faWQiOjIwMiwiZmlsZV9pZCI6Mzd9.YGG65Q.0NwTirE69YCv7yyLSx-X-1t3Iyo)

In the given file, code is given in php

<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/ciphertext.png" width = "1617" height = "250" >

</p>

Here we have two cipher texts, which are separated by @@

>> from this we can tell that all characters are uppercase letters. 

<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/Selection_014.png" width = "670" height = "270" >

</p>

<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/Selection_015.png" width = "640" height = "119" >

</p>

>> repeated xor :
<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/Selection_016.png" width = "760" height = "109" >

</p>


Here we have two cipher texts, try to built a code which allows uppercase letters and xor cipher texts and flag. till now we know that the flag = "UDCTF{" (with length = 6)
Try to guess letters one by one and xor it with cipher texts accordingly.

<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/Selection_018.png" width = "1150" height = "533" >

</p>

<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/Selection_020.png" width = "1009" height = "622" >

</p>

<p align="left">

<img src = "https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/crypto/BlueHensCTF/asset/flag(otp).png" width = "1129" height = "510" >

</p>

##Flag= UDCTF{w3lcome_t0_0ur_ctf}




