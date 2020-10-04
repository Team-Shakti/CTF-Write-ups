# Knot-65

## Description

Mr Elliot Anderson has received a zip file from somewhere around. From a secret friend he got a transcript of some conversation. Help Mr. Elliot to get the secret flag. Once you get the password,convert it to lower case as password.

## Solution

So, we are given one password protected zip file and one text file. If you look carefully we can find that some of the characters in the text file are in uppercase. You can either write a python program or manually collect the uppercase letters. And we get IKNOWYARECOLLECTAINGLLUPPERCASELETTERFIRSTPARTOFTHEPASSWORDISLETTHEREBE

![upper](https://github.com/ksridevi2908/CTF-Write-ups/blob/master/docs/forensics/DarkCTF/Knot-65/1.png)

``` python
r = open("file.txt","r")
r = r.read()
part1=''
for i in r:
	if i.isupper():
		part1+=i
print(part1) 
```
![out](https://github.com/ksridevi2908/CTF-Write-ups/blob/master/docs/forensics/DarkCTF/Knot-65/2.png)

As mentioned in the description, after converting it to lowercase, we get iknowyarecollectainglluppercaseletterfirstpartofthepasswordislettherebe. And the first part of the flag is lettherebe.

We get the second part of the flag by running stegsnow. 

![snow](https://github.com/ksridevi2908/CTF-Write-ups/blob/master/docs/forensics/DarkCTF/Knot-65/3.png)

The second part of the flag is goodrainswithshining.

We find some homoglyph unicode characters towards the end of the text file. Collecting those characters we get the last part of the flag rainnnbow. 

![last](https://github.com/ksridevi2908/CTF-Write-ups/blob/master/docs/forensics/DarkCTF/Knot-65/4.png)

So, the final password is "lettherebegoodrainswithshiningrainnnbow". We use this password to open the password protected text file which contains some 8 digit numbers.

> 31060562 32641524 21475550 14066460 21666171 34073461 35044157 33661564 15046170 23032164 146764

This is octal-xlate encoding. We can decode these characters online from [here](https://www.paulschou.com/tools/xlate/)

And the flag is darkCTF{h0m0Glypw1tHooct4LxL4t3}



