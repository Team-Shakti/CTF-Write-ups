# EasyWrite

The past weekend I played N1CTF along with my teammates, I ended up spending most of the time in EasyWrite and Signin. In this writeup I’ll be explaining about my approach for the EasyWrite, so let’s get started!

## Initial Click

All the useful mitigation are enabled other than FORTIFY. Also, the libc version required is libc-2.31. In a nutshell, the binary does the follows:

1. Gives us the libc leak directly
2. We can input 0x299 bytes which is stored on the heap [chunk1]
3. Asks us to enter an address [addr1] where contents of chunk1 are copied to
4. Allocated a chunk of size 0x30 [chunk2]. We can write 0x2f bytes to this chunk.
5. chunk2 is freed.

From this I could deduce that overwriting free_hook could be the key. But it wasn’t really that easy.

## What did not work?

On the first try, I gave addr1 as free_hook_ and the contents of chunk1 as address of system/ shellcode what not. I ended up with a SIGSEV because this was bound not to work as the binary was executing the chunk1 address and NX was enabled. I couldn’t find any other targets for a long while.

Another thing to try out was the controlling tcache structure because we could utilize the write happening on chunk2. Basically, we had to control malloc to help us in getting an arbitrary write. How about getting an allocation on free_hook_ and then overwriting it to get a shell? Not that easy.

## Crux: Controlling Tcache

We know that it’s the tcache_perthread_struct (stored on the heap) which kind of keeps a track of the count of chunks are present in the bin and also which one to be recycled on the next call. But in the present scenario we cannot control it because we do not have any way to get heap leaks but we have the libc leaks. Is there any way to control this region if we are armed only with libc leaks?

I found a mmap’d address which stores the pointer to the [tcache_perthread structure] -0x10 address. If we could overwrite this address with a chunk1 which has our fake tcache_structure (where the next 0x30 size chunk to be recycled is our free_hook_) then we could get the desired arbitrary write. In my understanding this mmap region is the global Tcache pointer which stores the pointer to the tcache structure (one stored on heap). More details can be found on another writeup on the same which gives a detailed understanding: https://ctftime.org/writeup/24295 .

## What happened next?

Unfortunately, I was not able to complete the challenge during the CTF. Here, none of the one_gadgets come to handy so one must overwrite free_hook_ with system but then it would call free(system) => system(system) which is really not what we desire. My teammate and I did a lot of tries on this but found it out very late that one could get the arbitrary write at free_hook -0x8 and overwrite it with “/bin/sh\x00” + libc_system_address.

Nevertheless, this was a fun challenge as I really learned something new. Also, we must learn to read the source code when all the doors seem to be closed. 

## Exploit

```python

from pwn import *
p = process("./easy",env = {"LD_PRELOAD" : "./libc-2.31.so"})
p.recvuntil("Here is your gift:")
leak = int(p.recvline().strip(),16)
print(hex(leak))
libc_start = leak - 0x08ec50
log.info("libc_start = " + hex(libc_start))
system = libc_start + 0x055410
free_hook = libc_start + 0x00000000001eeb28
tls_tcache = libc_start + 0x1f34f0
fake_tcache = p64(0x0000000100000000) + p64(0)0x82+p64(0)+ p64(free_hook-0x8)
p.sendafter("Input your message:",fake_tcache)
p.sendafter("Where to write?:",p64(tls_tcache))
p.sendafter("Any last message?:","/bin/sh\x00"+p64(system))
p.interactive()
```