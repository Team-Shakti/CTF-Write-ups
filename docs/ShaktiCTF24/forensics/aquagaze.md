# Aqua Gaze

**Description**
Unravel the enigma within the file's depths, employing the subtle art of concealment to reveal its hidden message.

*** Author: [__m1m1__](https://twitter.com/__m1m1__1) ***


**Solution**
Extract the given chall file; you will get a sea.jpeg.
Binwalk the jpeg and extract the embedded zip file.
By using John, the password for the zip file will be cracked, which is 'angel1'.

```
the command for John to crack the zip file password:
./zip2john 7D353.zip > zip.txt
john zip.txt
```
[!alttext](images/zip_pass.png)

Extract the zip file using the password, and you will get an artofeye.jpg. When you use jsteg on the image, encoded text can be seen by decoding it, which will give the flag.

```
command for jsteg:
jsteg reveal artofeye.jpg
```
[!alttext](images/jsteg.png)

encoded text: c2hha3RpY3Rme3RoM19yM2RfczM0XzRuZF90aDNfNHJ0X29mXzN5M18xc19sb29rMW5nX2cwMGR9


Flag: `shaktictf{th3_r3d_s34_4nd_th3_4rt_of_3y3_1s_look1ng_g00d}`