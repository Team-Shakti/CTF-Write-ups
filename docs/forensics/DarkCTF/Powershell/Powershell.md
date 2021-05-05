# PowerShell

Solved by : Sridevi

## Description

I want to know what is happening in my Windows Powershell.

## Solution

We are given a .mp3 file. When we open the file, we get an error. So, let's use binwalk to extract the embedded files.

![power](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/DarkCTF/Asset/5.png)

Since the challenge name is PowerShell, let's see what is there in PowerShell.xml

![file](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/DarkCTF/Asset/6.png)

There is a base64 string. Let's see what we get after decoding it.

![base](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/DarkCTF/Asset/7.png)

**Flag: darkCTF{C0mm4nd_0n_p0w3rsh3ll}**


