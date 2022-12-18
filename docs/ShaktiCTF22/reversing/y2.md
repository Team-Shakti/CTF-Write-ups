# Y2 for win

### Challenge Description :

Have you ever dealt with so many limitations???
If not then here you go...

##### Author - k1n0r4

<hr>

### Solution

View the binary in ida and you shall see a funcrtion named constraints containing a lot of checks

![](https://i.imgur.com/9xy70pC.png)

Here make use of the tool [z3-solver](https://github.com/Z3Prover/z3)

##### Script - 

```python=

from z3 import *

a1 = [BitVec("a1%i"%i,8) for i in range(25)]

s = Solver()

s.add(a1[13] * a1[9] - a1[23] == 10401)
s.add(a1[0] + a1[5] * a1[2] == 9147)
s.add(a1[2] * a1[8] - a1[13] == 10340)
s.add(a1[7] + a1[6] - a1[23] == 138)
s.add(a1[18] + a1[15] - a1[14] == 70)
s.add(a1[19] - a1[12] * a1[24] == -5808)
s.add(a1[21] * a1[16] - a1[10] == 4726)
s.add(a1[4] * a1[17] - a1[22] == 13130)
s.add(a1[3] * a1[1] - a1[11] == 2395)
s.add(a1[20] + a1[3] * a1[11] == 5214)
s.add(a1[8] * a1[5] - a1[20] == 10332)
s.add(a1[0] - a1[16] - a1[16] == -68)
s.add(a1[22] + a1[13] - a1[6] == 103)
s.add(a1[18] - a1[12] - a1[21] == -54)
s.add(a1[10] * a1[15] - a1[9] == 13828)
s.add(a1[19] + a1[24] - a1[14] == 129)
s.add(a1[4] * a1[17] - a1[7] == 13140)
s.add(a1[8] + a1[14] - a1[1] == 154)
s.add(a1[23] + a1[17] - a1[9] == 69)
s.add(a1[19] * a1[10] + a1[3] == 12901)
s.add(a1[5] + a1[21] * a1[12] == 2696)
s.add(a1[6] - a1[1] + a1[24] == 167)
s.add(a1[0] + a1[4] * a1[15] == 13577)
s.add(a1[7] - a1[18] - a1[20] == -81)
s.add(a1[7] - a1[18] - a1[20] == -81)
s.add(a1[9] + a1[19] * a1[8] == 11975)
s.add(a1[10] - a1[23] + a1[0] == 192)
s.add(a1[14] + a1[21] * a1[3] == 2594)
s.add(a1[16] + a1[12] + a1[1] == 197)
s.add(a1[6] + a1[20] - a1[13] == 110)
s.add(a1[5] - a1[21] + a1[16] == 139)

if s.check()==sat:
    m = s.model()

    flag = [chr(int(str(m[a1[i]]))) for i in range(len(m))]

    print(''.join(flag))

```

###### Output - z3_1s_fUn_wh3n_u_s0lv3_1t

<br>

Correct Input - z3_1s_fUn_wh3n_u_s0lv3_1t
##### Flag - shaktictf{z3_1s_fUn_wh3n_u_s0lv3_1t}