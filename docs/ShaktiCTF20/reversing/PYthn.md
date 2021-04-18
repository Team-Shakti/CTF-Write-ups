# PYthn


### Challenge description
 Familiar with python?

**Author**:[bl4ck_Widw](https://twitter.com/N4m1th4_01)

### Writeup

The challenge is really basic and simple for people who are familiar with python programing. The program need to be reversed to get the flag . 
The source code:

```
Z=[]
k=[]
Q="K78m)hm=|cwsXhbH}uq5w4sJbPrw6"
def Fun(inp):
    st=[]
    for i in range (len(inp)):
        st.append(chr(ord(inp[i])^1))
    return(''.join(st))
def FuN(inp):
    for i in range(len(inp)):
        if(i<11):
            Z.append(chr(ord(inp[i])+i+5))
        else:
            Z.append(chr(ord(inp[i])+4))      
    return(''.join(Z))
def fuN(text,s): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if(char.isnumeric()):
            result+=(chr(ord(char)-1))
        elif(char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        else: 
            result+=(chr(ord(char)^1))
    return result 
X=input("Enter input:")
k=FuN(Fun(X))
if(Q!=k):
    print("NO")
else:
    print("Flag: shaktictf{"+X+"}")
      
```
Here the variable k , is getting a string returned from two functions - FuN() and Fun(). (Note that function fuN is never used )
The input is simply passed on to the two functions and and the ouptput 'k' is compared with the string 'K78m)hm=|cwsXhbH}uq5w4sJbPrw6'. All we have to do is , find the input from this by reversing the functions to get the flag . 

Solution script:

```
y=[]
Z=[]
k=[]
Q="K78m)hm=|cwsXhbH}uq5w4sJbPrw6"
def Fun(inp):
    st=[]
    for i in range (len(inp)):
        st.append(chr(ord(inp[i])^1))
    return(''.join(st))
def FuN(inp):
    for i in range(len(inp)):
        if(i<11):
            Z.append(chr(ord(inp[i])-5-i))
        else:
            Z.append(chr(ord(inp[i])-4))      
    return(''.join(Z))


k=Fun(FuN(Q))
print("shaktictf{"+k+"}")

```

>flag : shaktictf{G00d!_c0nTinUe_Expl0r1nG_Mor3}
