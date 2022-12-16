## Challenge Title: cAex0r

### Challenge Description :
I tried to develop a new generator but I am not sure how it is working. Need some conformation.

### Difficulty Level
Easy

### Points
100

### Flag format 
shaktictf{...}

### Writeup
1. This is the combination of ceaser cipher and xor. 
2. Ceaser cipher funtion is already given. Length of key is 3. only thing to do brute force 
3. First 9 letters in the plain text are already known.`shaktictf{` 
4. Use known plaintext method and bruteforce the `stride` within the range of 1,27.
5. xor `sha` , each stride to get the key and `xor(ct,key)` to get the plaintext.
6. check `shaktictf{` in plaintext if `yes` then print the plaintext.



### Flag
`shaktictf{welCom3_t0_cRyptOo_WoRLD_77846b12bfd9b91ebce67b236aa4}`

### Author
Pavani





