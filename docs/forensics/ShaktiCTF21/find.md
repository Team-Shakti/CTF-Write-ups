# Find Me

### Challenge Description

We found that there was a secret communication between two criminals. Can you find out the secret information?

### Challenge Author

[v1Ru5](https://twitter.com/SrideviKrishn16)

### Short Writeup

Following up the TCP stream gives us this:
98 106 66 48 100 71 103 48 100 71 86 104 78 88 107 61

On converting the numbers from decimal to ASCII gives us 'bjB0dGg0dGVhNXk=' which when base64 decoded gives 'n0tth4tea5y'. The second TCP stream gives us a reversed zip file which after reversing back and using 'n0tth4tea5y' as the password gives us flag.txt.

### Flag

shaktictf{g00d_lUcK_4_tH3_n3xT_cH411eNg3}
