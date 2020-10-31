# Emojis - Misc HSCTF2020

## Description

We are given a binary which takes a string input and multiple math checks are performed on the input and had a good address which had to be achieved. The solution was obtained using a simple angr find and avoid script. 

### Solution Script
``` python
import angr
import claripy
import sys
proj=angr.Project('./jack',load_options={'auto_load_libs':False},main_opts={'base_addr':0x400000})
flag=[claripy.BVS('flag%i'%i,8) for i in range(16)]
flag_concat=claripy.Concat(*flag + [claripy.BVV("\n")])
state=proj.factory.entry_state(stdin=flag_concat)
for i in flag:
    state.solver.add(i>=32)
    state.solver.add(i<=127)
simgr=proj.factory.simgr(state)
simgr.explore(find=0x401489,avoid=[0x4012B3, 0x401468])
if simgr.found:
    simulation=simgr.found[0]
    print(simulation.posix.dumps(sys.stdin.fileno()))
else:
    print("FAILURE")
 
```

### Output 

`n0_5ymb0l1c,3x30`

This output was enclosed in the flagformat and submitted
