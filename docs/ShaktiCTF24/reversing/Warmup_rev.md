# Warmup Rev

### Description

Look Carefully! What you want lies inside straight in front of your eyes!

<br> 

Author: [k1n0r4](https://twitter.com/k1n0r4)

Difficulty level: Beginner

Points: 100

Category: Reverse Engineering


###  Solution

The given file is an ELF 64 bit binary. Let's use a decompiler to decompile the binary.

![image](https://imgur.com/wr4u3XL.png)

The logic under `main` function indicates that binary inputs the flag, reverses it and compares against a hardcoded string.

On reversing the given string, we retrive the flag.

```python
print("}!d33dn1_3gn3ll4hc_pUmr4w_4_51_s1ht{ftcitkahs"[::-1])
```

### Flag

`shaktictf{th1s_15_4_w4rmUp_ch4ll3ng3_1nd33d!}`