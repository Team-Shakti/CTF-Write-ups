# Quickfix 

## Description

We were given 10000 images which had to be fixed/concatenated together to form one final image of png format even though the given images were with .jpg file extension and showed that it was curropted when you tried to execute it. So basically first we get all the images, and change the header by changing the first 8 bytes and replace it with the first 8 bytes of png files. Then we rename all the files by changing their file extensions and last but not the least we concatenate the images as a 100x100 matrix image using the PIL module in python. 

### Solution Script
``` python
from __future__ import print_function
import os

from PIL import Image
def write_to():
    files = os.listdir('./QuickFix')
    ims=Image.open('./QuickFix/'+files[0]+'')
    result = Image.new("RGB", (100*ims.width, 100*ims.height))
    for i in range(100):
        for j in range(100):
            cur = Image.open('./QuickFix/'+'flag_{}_{}.png'.format(i,j))
            result.paste(cur, (i*ims.width,j*ims.height))
    result.save(os.path.expanduser('~/image.png'))
def header_change():  
    for i in os.listdir('./QuickFix'):          
        with open('./QuickFix/'+i,"rb+") as image:   
            f=image.read()   
            b=bytearray(f)   
            #print(b[:14])   
            b=b.replace(b[:14],b'\x89PNG\r\n\x1a\n\x00\x00\x00\r') 
            #print(b[:14]) 
            image.seek(0) 
            image.write(b)   
            image.truncate()  
def rename_func():
    for i in os.listdir('./QuickFix'):  
        os.rename('./QuickFix/'+i, './QuickFix/'+i[:-4]+'.png') 
```

## Solution

Flag: [Flag Image](image.png)

#
