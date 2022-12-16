
## Challenge Title: d0uble_cbc

### Challenge Description :
My uncle has been working as a schoolteacher. One fine day, he decides to give chocolates to all his students. He brought a different types of chocolates. But two students are asking for the same kind of chocolate. All chocolates of that kind are completed except one. So, he decided to change the chocolate wrapper and give the same chocolate that he has.Can you help him to find that same chocolate wrapper?
### Difficulty Level
Medium

### Points
200

### Flag format 
shaktictf{...}

### Writeup
1. This chall is combination of two iv detection in cbc mode and cbc mac vulnerability with non zero IV.
2. Find iv using the oracle provided and use that iv as input for cbc mac oracle.
3. iv detection can done by encrypting the `pt='\x00'*32` , decrypt `ct = b"\x00"*16+bytes.fromhex(ct)[:16]` , decrypt the result again to get iv. 
4. Now pass that iv to the sign function.It will return the tag as ct[16:].
5. sign(sign(block0) xor block1) gives the same sign value. (So, simply append the ciphertext of the previous block)


### Flag
`shaktictf{double_cheese_double_mac_yummyyyy_4120686170707920636263206d6f6465}`

### Author
Pavani





