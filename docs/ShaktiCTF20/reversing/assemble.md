# Assemble!

**Challenge author**[imm0rt4l_5t4rk](https://twitter.com/SimranKathpalia)

**Challenge points:** 200

**Challenge solves:** 13

### Challenge Description
Your input is your flag. <br>
Flag format: shaktictf{input1,input2,input3}

### Solution

We have to input three numbers which pass a series of conditions which on the end should give us `Correct` as an output. 

So here, `ebx` contains our 2nd input and `DWORD[ebp-0x4]` is our first input. And their sum should be equal to 0xdeadbeef.

```asm
mov ebx, DWORD[ebp-0xc]
add ebx, DWORD[ebp-0x4]
cmp ebx,0xdeadbeef
jne N
```
Then we put a condition on our first input and second input. Our first input should be less than 0x6f56df65. And our second input should be 0x6f56df8d. So we find that our first input becomes 0x6f56df62(keeping in mind the above condition).

```asm
cmp DWORD[ebp-0x4], 0x6f56df65
jg N

cmp DWORD[ebp-0xc], 0x6f56df8d
jg N
cmp DWORD[ebp-0xc], 0x6f56df8d
jl N
```

Onto finding our third input, we see that our second input is being xored with our third input. We already know our second input so our third input is 1867964301 ^ 2103609845 which is 305419896

```asm
mov ecx, DWORD[ebp-0x14]
mov ebx, DWORD[ebp-0xc]
xor ecx, ebx
cmp ecx, 2103609845
jne N
```

### Flag
shaktictf{1867964258,1867964301,305419896}