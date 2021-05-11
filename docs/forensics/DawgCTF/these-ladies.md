## These Ladies Paved Your Way 
##### Challenge Descritpion:
Per womenintech.co.uk, these 10 women paved your way as technologists. One of them holds more than 100 issued patents and is known for writing understandable textbooks about network security protocols. What other secrets does she hold?
[Challenge file](https://umbccd.io/files/10fe5bdd1c030ec8b66de1dc6fb20492/WomenInTech.zip?token=eyJ1c2VyX2lkIjo4NTcsInRlYW1faWQiOjE4MiwiZmlsZV9pZCI6N30.YJrDhA.nda6buQjEdhDp0poyyeTgEJH7gg)
- On analysing the given zip file we find many images of women
- On googling about ```100 issued patents and is known for writing understandable textbooks about network security protocols``` , we find that its related to ```Radia Perlman``` and we find an image named ```radia_perlman.jpg``` in zip file
- Running exiftool on the image we find ```VpwtPBS{r0m5 0W t4x3IB5}```(looks like a potential flag) and ```U3Bhbm5pbmdUcmVlVmlnCg==```
- On b64decoding the latter text, we get the key 'SpanningTreeVig'
- And then it's just a vignere cipher decoding and we get the flag 
```
DawgCTF{l0t5 0F p4t3NT5}
```