# BomB 


##### Challenge Author :bl4ck_Widw
##### Points :200



#### Description
flag format : shaktiCTF{S0m3_stR1nG}

### WriteUp

This a  basic C++ challenge which uses xoring to form the flag from the input .While running the program , we can see that the binary asks for a pin code.
Going in deep into the program , we can see that there is a comparison of the input length with 9 . 

Further , when you move through the rest of the code , we can see that the input pin code gets xored with a string:
```
 '\x10\x13\x17m\x17\x13\x03' 
```
its output again gets xored with an array :
```
[85, 76, 66, 53, 80, 72, 118, 98, 59, 78, 98, 126, 5, 107, 100, 75, 110, 60, 123, 16, 17, 105, 57, 6, 119, 85, 98, 93, 112, 16, 87, 109, 96, 126, 82, 100, 78, 1, 98, 105, 65, 4, 116, 79, 2, 35]
```

This finally gives us the output, which if passes the constrains given, provides us with the flag . 
As the challenge discription tells us about the flag format , we can use it as a clue in solving our problem. 

As we know , the flag format is shaktiCTF{} .
ShaktiCTF is  a 9 letter long string just like our input . Hence we can use the flag format to reverse our program and find the pin . 
Solution script:
```
d="shaktiCTF"
# The flag format can be used to find the pin code 
c=[85, 76, 66, 53, 80, 72, 118, 98, 59, 78, 98, 126, 5, 107, 100, 75, 110, 60, 123, 16, 17, 105, 57, 6, 119, 85, 98, 93, 112, 16, 87, 109, 96, 126, 82, 100, 78, 1, 98, 105, 65, 4, 116, 79, 2, 35]
xored1 = []
for i in range(len(d)):
    xor=chr(ord(d[i%len(d)]) ^ c[i])
    xored1.append(xor)
a=[0x10, 0x13, 0x17, 0x6d, 0x17, 0x13, 0x3, 0x0,0x4b,0x3,0x1,0x2,0x5, 0x7]
xored4 = []
print("PIN: ")
for i in range(0,9):
    Output=chr(ord(xored1[i%len(xored1)]) ^ a[i])
    xored4.append(Output)
print(xored4)

#pin :674332666
``` 
```
flag :shaktiCTF{TH3_BoMb_1$_D3AcTiV4t3D_gR34T_w0Rk!}
```
