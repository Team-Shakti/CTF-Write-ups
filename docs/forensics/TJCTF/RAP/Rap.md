# Rap Goad

Solved by : Sridevi

## Description

My rapper friend Big Y sent me his latest track but something sounded a little off about it. Help me find out if he was trying to tell me something with it. Submit your answer as tjctf{message}

## Solution

Open the given mp3 file using Sonic Visualiser. Using Spectrogram we see something like this.

![img1](https://github.com/ksridevi2908/CTF-Write-ups/blob/master/docs/forensics/TJCTF/Rap%20God/img1.png)

They are encoded images, but not clear. Let's examine the channel-2 in Spectrogram. Now, the encoded symbols are clear.

![img2](https://github.com/ksridevi2908/CTF-Write-ups/blob/master/docs/forensics/TJCTF/Rap%20God/img2.png)

After surfing through internet I came across [this](https://www.dcode.fr/wingdings-font) website which decodes similar images as in our case. Let's try decoding using this website.

tjctf{quicksonic}

We got the flag!
