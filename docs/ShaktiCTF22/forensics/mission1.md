# Mission 1 

### Challenge Description

You are a forensics investigator hired by a private comapny to gather proofs against an ex-employee who secretly worked for the rival company and was fired later. This memory dump was taken from the ex-employee's system. Answer the following questions as a part of your mission:
 
1. What is the sha1 hash of Challenge.raw?
2. What is the user password of TroubleMaker's account?
3. What is the PID of the program used to capture the image?

### Challenge Author

[v1Ru5](https://twitter.com/SrideviKrishn16)

### Writeup

The first part of the challenge is pretty easy. This gives us the sha1 hash of the challenge file.

```
sha1sum Challenge.raw
```
We use volatility for the remaining part of the challenge. To start with, we use imageinfo to find the profile of the given memory dump.

![img1](image1.png) 

To get the user password, we use "hashdump" plugin and crack TroubleMaker's password hash using crackstation. We get the password as "londonbridge".

```
volatility -f Challenge.raw --profile=Win7SP1x64 hashdump 
```

![img2](image2.png) 

To get the last part of the flag, we use pslist plugin which lists out all the processes that were running during the memory capture. Dumpit was the tool used for image capture and the corresponding PID is 636. 

### Flag

shaktictf{ed85ee47484e503787277807d3ef999586aecf1b_londonbridge_636}
