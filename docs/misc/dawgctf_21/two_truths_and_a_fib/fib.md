# Two truths and a fib



### DESCRIPTION:
![about](../../two_truths_and_a_fib/about.png)


#### SOLUTION:

* When we connect:

![about](../../two_truths_and_a_fib/run.png)

* The program asks us to choose the fibinoaci numbers out of the given numbers. 

#### Script:
```
def fib(l) : 
    ans = [] 
    for i in l : 
        y = [is_square((5*i*i) + 4 ),is_square((5*i*i) - 4)] 
        if 1 in y : 
            ans.append(i) 
    return ans 
     
def connect() : 
    r = remote('umbccd.io', 6000) 
    while(True) : 
        print(r.recvuntil("[")) 
        l = list(map(int,r.recvline().decode().strip()[:-1].split(", "))) 
        print(l) 
        ans = fib(l) 
        for i in ans : 
            r.recv() 
            r.sendline(str(i))  
```

#### FLAG:
DawgCTF{jU$T_l1k3_w3lc0me_w33k}
