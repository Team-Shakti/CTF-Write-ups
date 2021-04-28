# Help Me 

### Challenge Description

Our department had taken up the responsibility of solving a mysterious case but unfortunately our system crashed. We could only recover this memory dump. Your job is get all the important files from the system and use the files to find out the secret informatiom.

### Challenge Author

[v1Ru5](https://twitter.com/SrideviKrishn16) & [bl4ck_Widw](https://twitter.com/N4m1th4_01)

### Short Writeup

We use the tool 'volatility' for this challenge. This command gives us the first part.

```
volatility -f Challenge.vmem --profile=Win7SP1x64 cmdscan
```

Which on base64 decoded gives us 'shaktictf{H0p3'.

```
volatility -f Challenge.vmem --profile=Win7SP1x64 filescan 
```

shows that there are two useful files Part II.png and L4ST.py.zip. Extract both the files. Apply 'zsteg' on the PNG image and we got the second part of the flag "_y0U_l1k3d_
". The zip file has a python script which needs to be reversed. 

```
def tryin(text,s): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if(char.isnumeric()):
            result+=(chr(ord(char)+1))
        elif(char.isupper()): 
            result += chr((ord(char) - s-65) % 26 + 65) 
        else:
            result+=(chr(ord(char)^1)) 
    return result 
def checkin(inp):
    for i in range(len(inp)):
        if(len(inp)<=7):
            Z.append(chr(ord(inp[i])-i+1))
        else:
            Z.append(chr(ord(inp[i])-4))      
    return(''.join(Z))
    # Giving the input "y>v<^xd::439064..y" as the string from the challenge , gives us our input to be used:
X="uh27bio:uY<xrA."
s=4
y=[]
Z=[]
Y=[]
k=[]
X=checkin(X)
y=tryin(X,s)
print("input: "+y)
```
which gives the last part of the flag "th15_ch4lL3ng3!}"

### Flag

shaktictf{H0p3_y0U_l1k3d_th15_ch4lL3ng3!}
