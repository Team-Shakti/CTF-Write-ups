# Operation Ultra

### Description

In "Operation Ultra," Agent Evelyn "Eclipse" is on a mission to recover the vanished scientist, Dr. Viktor Kozlov, and secure his groundbreaking energy technology research.

**Author: [k1n0r4](https://twitter.com/k1n0r4)
Difficulty level: Easy
Points: 200
Category: Reverse Engineering**

###  Solution


- Decoding the base64-encoded string, unk_str we retrieve the key `Shadows2024`.
- The `func_1` is called with arguments unk_str and the input flag (`unk_str0`). Within this function, a XOR operation is performed on each character from unk_str0 with a repeated sequence of `unk_str`.
- The output of `func_1` (`unk_str1`) is passed to `func_2`, where an empty list (`unk_str3`) is initialized.
- In two loops, characters from `unk_str1` are selected at specific indices in `unk_str3`, constructing a new string (`unk_str2`) which is then returned. The operation performed is shuffling where elements from alternative positions are picked up and appended to a list.
- This final string (`unk_str2`) is compared with a predefined set of ASCII values (`unk_arr0`). If the comparison is successful, the input is considered correct.

#### Solution script
When reversing `func_2` by inputting the given ASCII values and performing the same operations, we obtain the input to `func_2`. Upon XORing this input with Shadows2024, the flag is obtained.

``` python 
def func_2():
    unk_str3 = [32, 0, 27, 30, 84, 79, 86, 22, 97, 100, 63, 95, 60, 34, 1, 71, 0, 15, 81, 68, 6, 4, 91, 40, 87, 0, 9, 59, 81, 83, 102, 21]
    flag_len = len(unk_str3)
    unk_str0 = ['']*flag_len

    j = 0

    for i in range(0, flag_len , 4):
        unk_str0[i] = unk_str3[j]
        unk_str0[i + 1] = unk_str3[j + 1]
        j += 2

    for i in range(2, flag_len, 4):
        unk_str0[i] = unk_str3[j]
        unk_str0[i + 1] = unk_str3[j + 1]
        j += 2

    return unk_str0
unk_str1=func_2()
print(unk_str1)
```
```
Output:

[32, 0, 0, 15, 27, 30, 81, 68, 84, 79, 6, 4, 86, 22, 91, 40, 97, 100, 87, 0, 63, 95, 9, 59, 60, 34, 81, 83, 1, 71, 102, 21]
```


```python
li=[32, 0, 0, 15, 27, 30, 81, 68, 84, 79, 6, 4, 86, 22, 91, 40, 97, 100, 87, 0, 63, 95, 9, 59, 60, 34, 81, 83, 1, 71, 102, 21]
a="Shadow2024Shadow2024Shadow2024Shadow2024"
for i,j in zip(li,a):
  print(' '.join(chr(i^ord(j))),end="")
```

### Flag

`shaktictf{Ul7r4_STe4l7h_SUcc3s5}`