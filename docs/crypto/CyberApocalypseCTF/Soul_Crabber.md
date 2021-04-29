# Soul Crabber

Solved by: Sowmya (@__4lph4\_\_) , Ashwathi (@Ashwathi_sasi) , Namitha (@N4m1th4_01)

The rust code takes input and xor's it with random numbers. Since the seed is same, the series of random numbers generated is same each. So we could run it against a dummy input and xor it with the output to get the series of random no. generated. This array when xored with the given output will give us the flag

Solution Script: 
```python
    f2 = []
    dummy_out = "296625b4d4823f73ddd35926ed1839d44c381878c6e19969620e99e36b196f"
    dummy_in = "qwertyuiopasdfghjklzxcvbnmqwe"
    for i in range(0,len(dummy_out),2):
        f2.append(int("0x"+dummy_out[i:i+2],16))
    rand_arr = []
    for i in range(len(dummy_in)):
        rand_arr.append((f2[i])^ord(dummy_in[i]))
    fout = "1b591484db962f7782d1410afa4a388f7930067bcef6df546a57d9f873"
    fo2 = []
    for i in range(0,len(fout),2):
        fo2.append(int("0x"+fout[i:i+2],16))
    f= ""
    for i in range(len(rand_arr)):
        f=f+chr(fo2[i]^rand_arr[i])
    print(f)
```

Flag: CHTB{mem0ry_s4f3_crypt0_f41l}