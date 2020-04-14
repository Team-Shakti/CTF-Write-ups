# Auto_bot

when we connected to server we got base64 encoded binary. Using bash we recieved the decoded binary and anylised it. But each time it was a new binary. 
Heres the scritp
```
from pwn import *
import base64
import subprocess
import angr
import sys
r = remote('pwn.byteband.it', 6000)
flag = open('flag.txt', 'w')
while(1):
    o = r.recvuntil("\n")
    flag.write(str(o))
    out = base64.b64decode(o)
    n=open("new","wb")
    n.write(out)
    n.close()
    subprocess.call(['chmod','+x','new'])
    project = angr.Project("./new")
    initial_state = project.factory.entry_state()
    simulation = project.factory.simgr(initial_state)
    simulation.explore(find = lambda s: b"good job" in s.posix.dumps(1) in s.posix.dumps(1))
    if simulation.found:
        solution_state=simulation.found[0]
        r.sendline(solution_state.posix.dumps(sys.stdin.fileno()))
        #in = inp[2:len(inp)-1]
    else:
        raise Exception('could not find solution:')
    #r.sendline(in)
#flag{0pt1mus_pr1m3_has_chosen_you}

```
