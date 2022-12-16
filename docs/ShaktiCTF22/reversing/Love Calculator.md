# Love Calculator

### Challenge Description :

Here is something you always wanted to stumble upon, A Love Caluculator...Go on and check your luck.

##### Author - k1n0r4

<hr>

### Solution

We are provided with a binary and on opening the binary in IDA disassembler and decompiler we see the following pseudo code.

![](https://i.imgur.com/25Hd8uz.png)

The binary asks for two inputs - your name and your crush's name. But regardless of our input it displays the message 

![](https://i.imgur.com/SR0AUci.png)

Next it asks for a passkey which is actually the correct flag. Thus, our aim is to provide a desired input which would enable the binary to display the win statement.

![](https://i.imgur.com/uQVZLS8.png)

Our input passkey is being compared with a char array named as v9 here( the name would differ from user to user).

![](https://i.imgur.com/aVG8EDb.png)

v9 is being initialized before the check. The entire passkey is divided into several small parts, those parts are initialized to different char arrays and then the entire thing is concatenated in a particular order.

Correct Input - l3t5_s0lv3_m0r3_ch4ll3ng3s
Flag - shaktictf{l3t5_s0lv3_m0r3_ch4ll3ng3s}