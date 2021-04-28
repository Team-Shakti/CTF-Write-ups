### Author

Simran Sandra

### Challenge Short Writeup

The challenge was a packed GoVM binary which had a hidden flag. The intended solution to the challenge being, to solve the challenge the intended solution is to go through the binary and find out the conditions to be satisfied for the input to satisfy and add the constraints to the z3 solver. 

### Solver

```python
result = [165,72,3104,3424,3712,3360,3168,107,104448,203,98,119808,105,127,102,106,196,114,98,160,177,167,68,53,111,3200,99,150,127,3520,39,118784,95,72,99328,120832,42,175,77,167,99,104,175,118784,17,100,1632,86,148,69,3712,127,7,95,181,123904,127,104,43,91,127,111616,147,66,103,43,116736,1632,118784,111,73728,52,77,17,92,135,79,110,17,93]
opcode = [4, 8, 3, 3, 3, 3, 3, 6, 2, 5, 4, 2, 6, 8, 4, 6, 5, 7, 4, 4, 5, 4, 1, 7, 1, 3, 4, 4, 8, 3, 6, 2, 7, 8, 2, 2, 6, 5, 8, 4, 7, 7, 5, 2, 8, 6, 3, 6, 4, 1, 3, 8, 1, 6, 5, 2, 8, 7, 6, 6, 8, 2, 4, 1, 7, 6, 2, 3, 2, 1, 2, 7, 8, 8, 1, 5, 8, 7, 1, 8]
import math
def xor(argument):
  return argument^0x30
def mult(argument):
  return math.ceil(argument/1024)
def mul(argument):
  return math.ceil(argument/0x20)
def division(argument):
  return math.ceil(argument-0x32)
def add(argument):
  return argument-0x50
def sub(argument):
	return argument+0x9
def div(argument):
	return argument
def andd(argument):
	return argument^0x20
def default(argument):
  return "Incorrect case"
switcher = {
    1: xor,
    2: mult,
    3: mul,
	4: division,
    5: add,
    6: sub,
	7: div,
	8: andd
}
def switch(operation, num1):
  return switcher.get(operation, default)(num1)
flag=[]
for i in range(80):
	flag.append(switch(opcode[i], result[i]))
flag=[chr(int(k)) for k in flag]
print(flag)

```

### Flag 

`shaktictf{0ur_4str0naut5_d1d_n0t_hav3_much_t1m3_but_7hey_h4d_marg4r3t_H4m1l7on!}`
