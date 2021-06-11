# A Small Maniac's game

* points - 100

# Description :
```
A game that zh3r0 guys asked for 😥

Note: Solve all the levels and then click submit the solution button and wait for 40 seconds to get the flag. 
```

# Solution :

### level 0: here we make use of "MOVE A1 A2" instruction where in A1 is the amount of steps and A2 is the direction.

![level 0](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%200.png)

### level 1: same instructions are used to navigate here too. 

![level 1](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%201.png)

### level 2: "READ A1" will read the input and store it into A1 whereas "UNLOCK A2" has key = A2 which is used to unlock the door. 

![level 2](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%202.png)

### level 3: the instruction "ADD M1 A1 A2" stores the result of A1+A2 into M1. And so other operations of subtraction and multiplication are also obtained.

![level 3](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%203.png)

### level 4: "JMP A1" will allow us to jump to a line in the code.

![level 4](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%204.png)

### level 5: 

![level 5](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%205.png)

### level 6: "JMPZ A1 A2" jumps to line A1 if A2 is 0, whereas "JMPN A1 A2" jumps to line A1 if A2 is negative.

![level 6](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%206.png)

### level 7: moving in the clockwise and solving the equation.

![level 7](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%207.png)

### level 8: "CMP M1 A1 A2" is used to compare A1 and A2. If A1 > A2 then M1 = 1; if A1 = A2 then M1 = 0; if A1 < A2 then M1 = -1

![level 8](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%208.png)

### level 9: we make use "JMP" instructions to run a loop.

![level 9](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%209.png)

### level 10: "[[2]]" implies double dereference. i.e if 2nd register contains 3 and third register contains 54, then "[[2]]" will evaluate to 54.

![level 10](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%2010.png)

### level 11: register "[7]" contains number of steps taken. It doesn't increment once it hits a block.

![level 11](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%2011.png)

### level 12: we can use all the above instructions to run a loop in order to check if the input is prime or not. 

![level 12](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/level%2012.png)

## Flag :

![flag](https://github.com/shravya-bhaskara/CTF-s/blob/main/zh3r0CTF/flag.png)


