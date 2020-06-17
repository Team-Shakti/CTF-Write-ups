# Emojis - Misc HSCTF2020

## Description

This challenge was made using emojigram language which is an esolang made using Emojis. All that we need to do is repicate the code in python and generate the flag from it by reversing the code.

### Replicated Code

The replicated code looked like this.
But since there are conditional jumps and all that we are given is the output when the flag is given, we have no choice but to guess whether the jumps are taken or not inorder to obttain the desired input.
And to achieve the same we played around with a few of the instructions and put together the possibilities to get the Flag.

```python

flag=[120, 66, 94, 114, 95, 69, 110, 125, 73, 78, 99, 52, 118]
flag[9]=flag[9]+flag[1]
flag[7]=flag[7]+flag[11]
flag[2]=47
flag[4]=flag[4]+flag[11]
flag[0]=flag[0]+flag[2]
flag[8]=flag[8]-8
flag[6]=flag[6]+flag[8]
flag[6]=flag[6]-flag[8]
flag[6]=flag[6]-flag[8]
flag[10]=flag[10]+8
flag[11]=flag[11]-1
flag[4]=flag[4]-flag[9]
flag[3]=flag[3]-2
flag[2]=flag[2]-4
flag[0]=flag[0]-flag[11]
flag[1]=flag[1]-flag[3]
flag[1]=flag[1]+flag[3]
flag[1]=flag[1]+flag[3]
flag[1]=flag[1]-flag[7]
flag[3]=flag[12]
flag[2]=flag[2]+8
flag[9]=flag[9]-flag[6]
flag[2]=flag[2]+flag[4]
#flag[1]==flag[5]
#False
flag[2]=flag[5]
#flag[1]==flag[12]
#False
#flag[11]=flag[11]+flag[0]
flag[12]=118

```
## Solution

`Flag: flag{tr3v0r-pAck3p}`

#
