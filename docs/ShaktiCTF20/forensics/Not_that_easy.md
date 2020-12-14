# Not That Easy

### Challenge Description

We have intercepted the communication between two criminals and we found that they had shared a secret information. Can you find out the secret?

### Short writeup

There are a set of TCP packets with some data present in their buffer that eventually leads us to the wrong flag. The packet with size 521 bytes begins with file signature -> 89 50 4e 47 0d 0a....which is a PNG image. Extract the image and use zbarimg to view the flag.

### Challenge Author

[v1Ru5](https://twitter.com/SrideviKrishn16)

### Flag

shaktictf{sh3_w4s_h0n0r3d_by_3lectr0nic_fr0nti3r_f0und4ti0n}
