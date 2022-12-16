### Eazy_peaZy
### Challenge Description :
Who knew encryption could be so simple?



### Difficulty Level
Beginner

### Points
50
 
### Flag format 
shaktictf{...}

### Author
Rees

### Writeup
This is the combination of base64 and shifting

```python!
from base64 import b64decode

x = 'ZFlSXGVaVGVXbFRjamFlIVAiZFBkZmEkY1BWUmtqampqampQWFQlJCNlYyYnWCVlYyYlbg=='

x = b64decode(x)
flag = ''
for i in x:
    flag = flag + chr(i +15)

```
#### flag 
`shaktictf{crypt0_1s_sup3r_eazyyyyyy_gc432tr56g4tr54}`

