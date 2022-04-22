# Vanity

## Description

![desc](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/TAMUCTF22/Vanity/desc.png)

## Solution

We are given a gif in the description which gives us a hint "mirror". So we try

```
git clone --mirror https://github.com/tamuctf/vanity.git
```

Check out 'packed-refs', the last commit looks suspicious. Just clone the repository and 'checkout' the last commit. 

We have sneaky.txt. Opening sneaky.txt gives us the flag.

![flag](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/TAMUCTF22/Vanity/flag.png)

**gigem{watch_the_night_and_bleed_for_me}**

