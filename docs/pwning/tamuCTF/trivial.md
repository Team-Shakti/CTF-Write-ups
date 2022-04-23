

Tamuctf22
 
Trivial - pwn challenge
The challenge file for tamuctf is a zip which contains an elf trivial, a c file called trivial.c and a python file solver-template.py,.This exploit is done using gdb to get a better understanding.
The file trivial.c gives:
```
#include <stdlib.h>
#include <stdio.h>

void win() {
    system("/bin/sh");
}

void main() {
    char buff[69];

    gets(buff);
}
```

This is a ret2win challenge, where we can exploit the gets function in main to access win. gets is a library function which reads input from stdin until a newline character is read or the end of  file is reached.  So if we give enough junk data to fill the buffer, whatever is given after will overwrite the nearby memory. So if we overflow the stack and give the address of the win function as input, we can make the rip point to it. To do this, first take a look at disassembly of trivial.

![](https://i.imgur.com/70CUjxD.png)


As we can see the buffer size is 0x50, which is 80 is decimal . Now the buffer in the c file was given as 69, but here it is seen to be 80. This is because, in a 64 bit system ,when the file is compiled the memory allocated will be a multiple of 16  and so the buffer size was rounded off to the closest higher  multiple of 16, which was 80.
So we need to pass 0x50 bytes of junk data and  8 extra bytes to write the address on to the rip.The 8 extra bytes is used to overwrite the memory on rip.Find the address of the win function:
![](https://i.imgur.com/xI1GKej.png)


So we’ll input a string with 0x58 bytes of random data and the ret and win addresses. In 64 bit systems, the addresses are 8 bytes long and they are read by line. This may lead to some misalignment issues, so we add a return address along to prevent that error. The return address here will be the ret address.
The address of ret is:0x401160.
So the exploit will be :
```
! python -c 'print "A"*0x58+ "\x60\x11\x40\x00\x00\x00\x00\x00"+"\x32\x11\x40\x00\x00\x00\x00\x00"'|./trivial 
```

