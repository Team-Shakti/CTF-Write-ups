# NotBabyRev

### Description

I love challenges !!
Here is a Real Task for you.

<br>

Author: [k1n0r4](https://twitter.com/k1n0r4)

Difficulty level: Medium

Points: 300

Category: Reverse Engineering

###  Solution

The given file is a windows executable but on using a decompiler to decompile this binary does not give us much information. 

On executing the file, we get an interface which looks like this

![image](https://imgur.com/A4zJ38O.png)

So well, this is a flag checker. Let's try to analyse the source code of this binary.

Performing `strings` on the executable, gives up the output something like this

![image](https://imgur.com/Xu9CjBE.png)

This indicates towards the fact that the executable is [UPX packed](https://github.com/upx/upx). Unpack the binary using UPX and view it in a decompiler.

One easy way to go the main crux of the windows binaries is using strings and find the location of the crucial strings

![image](https://imgur.com/nbOUZaQ.png)

Here we find quite a lot of interesting strings, which can lead us to the important functions of the binary.

Well, seems like we found an important function `sub_140011BF0`

![image](https://imgur.com/6Lk4C5j.png)

Input is taken via the api `GetWindowTextA` into the variable `Src`.

Function `sub_1400110BE`seems some sort of check for it to print the win statement "Congratulations!!!"


![image](https://imgur.com/F3n8t9d.png)

On entering that function, we find the following operations being performed on the input taken

- Flag length check to be 36

![image](https://imgur.com/jCJFdbT.png)

- Characters at odd index number are xorred with 0x38 and stored in a new array `v8`

![image](https://imgur.com/JPRUWq8.png)

- Subtract 5 from each of the characters

![image](https://imgur.com/gpXVYSI.png)


- Convert the entire input of length 36 to 6X6 matrix

![image](https://imgur.com/H16pRvy.png)

- 4 Swaps
    - Swap 1: 1st and 4th row
    - Swap 2: 2nd and 5th column
    - Swap 3: 2nd and 6th row
    - Swap 4: 3rd and 4th column

![image](https://imgur.com/r2y90H0.png)

- Some constraints performed on the manipulated input

![image](https://imgur.com/Ju5Otos.png)




These constraints can be solved using a constraint solver called z3.

#### Solution Script



Here is the entire script - 



```py
from z3 import *

matr = [[Int(f'matr_{i}_{j}') for j in range(6)] for i in range(6)]

sol = Solver()

sol.add(matr[2][4] + matr[1][0] - matr[3][0] == 106)
sol.add(matr[5][2] + matr[1][4] - matr[4][5] == 174) 
sol.add(matr[0][2] + matr[5][4] - matr[2][5] == 111) 
sol.add(matr[3][0] + matr[2][2] - matr[4][4] == 19) 
sol.add(matr[1][3] + matr[3][5] - matr[0][2] == 16) 
sol.add(matr[3][3] + matr[0][1] - matr[4][3] == 75) 
sol.add(matr[0][5] + matr[4][2] - matr[1][0] == 111) 
sol.add(matr[2][1] + matr[3][2] - matr[5][3] == 83) 
sol.add(matr[1][2] + matr[4][3] - matr[4][2] == 113) 
sol.add(matr[3][2] + matr[0][2] - matr[0][5] == 89) 
sol.add(matr[4][2] + matr[2][5] - matr[5][5] == 141) 
sol.add(matr[1][0] + matr[0][5] - matr[2][3] == 115) 
sol.add(matr[2][2] + matr[4][5] - matr[5][1] == 18) 
sol.add(matr[5][0] + matr[4][1] - matr[0][3] == 155) 
sol.add(matr[0][0] + matr[3][3] - matr[3][1] == 84) 
sol.add(matr[3][4] + matr[1][1] - matr[2][1] == 31) 
sol.add(matr[1][5] + matr[2][3] - matr[4][0] == 187) 
sol.add(matr[4][3] + matr[0][3] - matr[1][1] == 102) 
sol.add(matr[0][4] + matr[2][1] - matr[5][2] == 51) 
sol.add(matr[2][5] + matr[4][4] - matr[2][2] == 141) 
sol.add(matr[1][4] + matr[3][1] - matr[0][0] == 102) 
sol.add(matr[5][5] + matr[3][4] - matr[3][2] == 40) 
sol.add(matr[0][1] + matr[4][0] - matr[2][0] == 22) 
sol.add(matr[4][4] + matr[1][5] - matr[1][2] == 109) 
sol.add(matr[3][5] + matr[3][0] - matr[4][1] == 95) 
sol.add(matr[1][1] + matr[0][0] + matr[5][4] == 184) 
sol.add(matr[4][1] + matr[2][0] - matr[0][1] == 60) 
sol.add(matr[3][1] + matr[1][2] - matr[3][3] == 96) 
sol.add(matr[5][3] + matr[5][0] - matr[1][4] == 73) 
sol.add(matr[0][3] + matr[5][5] + matr[5][0] == 135) 
sol.add(matr[4][5] + matr[2][4] - matr[1][3] == 130) 
sol.add(matr[2][3] + matr[1][3] + matr[3][4] == 179) 
sol.add(matr[5][4] + matr[5][1] - matr[0][4] == 87) 
sol.add(matr[2][0] + matr[0][4] - matr[2][4] == 83) 
sol.add(matr[5][1] + matr[5][3] - matr[3][5] == 64) 
sol.add(matr[0][0] + matr[0][1] + matr[0][2] + matr[0][3] + matr[0][4] + matr[0][5] == 458) 
sol.add(matr[1][0] + matr[1][1] + matr[1][2] + matr[1][3] + matr[1][4] + matr[1][5] == 425)
sol.add(matr[2][0] + matr[2][1] + matr[2][2] + matr[2][3] + matr[2][4] + matr[2][5] == 445)
sol.add(matr[3][0] + matr[3][1] + matr[3][2] + matr[3][3] + matr[3][4] + matr[3][5] == 526)
sol.add(matr[4][0] + matr[4][1] + matr[4][2] + matr[4][3] + matr[4][4] + matr[4][5] == 418)
sol.add(matr[5][0] + matr[5][1] + matr[5][2] + matr[5][3] + matr[5][4] + matr[5][5] == 522)
sol.add(matr[0][0] + matr[1][0] + matr[2][0] + matr[3][0] + matr[4][0] + matr[5][0] == 394)
sol.add(matr[0][1] + matr[1][1] + matr[2][1] + matr[3][1] + matr[4][1] + matr[5][1] == 382)
sol.add(matr[0][2] + matr[1][2] + matr[2][2] + matr[3][2] + matr[4][2] + matr[5][2] == 560)    
sol.add(matr[0][3] + matr[1][3] + matr[2][3] + matr[3][3] + matr[4][3] + matr[5][3] == 357)
sol.add(matr[0][4] + matr[1][4] + matr[2][4] + matr[3][4] + matr[4][4] + matr[5][4] == 599)
sol.add(matr[0][5] + matr[1][5] + matr[2][5] + matr[3][5] + matr[4][5] + matr[5][5] == 502)


if sol.check() == sat:
    model = sol.model()
    result_matrix = [[model.evaluate(matr[i][j]) for j in range(6)] for i in range(6)]
    print("Satisfiable solution found:")
else:
    print("No satisfiable solution found.")

matrix = [[0 for j in range(6)] for i in range(6)]

for i in range(6):
    for j in range(6):
        matrix[i][j] = result_matrix[i][j].as_long()

for row in matrix:
    print(row)


for i in range(6):
    matrix[i][2],matrix[i][3] = matrix[i][3],matrix[i][2]

for j in range(6):
    matrix[1][j],matrix[5][j] = matrix[5][j],matrix[1][j]

for k in range(6):
    matrix[k][1],matrix[k][4] = matrix[k][4],matrix[k][1]

for a in range(6):
    matrix[0][a],matrix[3][a] = matrix[3][a],matrix[0][a]

for b in range(36):
    matrix[b//6][b%6] += 5

for x in range(36):
    if x % 2 == 0:
        print(chr(matrix[x//6][x%6] ^ 0x38),end='')
    else:
        print(chr(matrix[x//6][x%6]),end='')

```

### Flag

`shaktictf{h0w_w4s_th3_fl4g_ch3ck3r?}`

