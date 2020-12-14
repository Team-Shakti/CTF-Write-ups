# Extract M3

### Challenge Description

We got a clue for a pending criminal case but seems like there was a secret exchange of information among the suspects. Can you help us find what they were sharing so that we can punish the criminals?

### Short writeup

Extract the data from TCP packets where the length of bytes is more than 900 and save it as a new pcapng file. Use scapy to extract the jpg image data from the new pcapng file.

```from scapy.all import *
r=rdpcap('newfile.pcapng')
s=''
for i in r:
	s+=i.load
open('image.jpg','w').write(s)
```

Extract the zip file using binwalk which is password protected. Use fcrackzip and rockyou.txt to find out the password and open the pdf file. Select the entire file and change the text colour to black to view the flag.

### Challenge Author

[v1Ru5](https://twitter.com/SrideviKrishn16)

### Flag

shaktictf{h0p3_y0u_ar3_enj0ying_thi5}
