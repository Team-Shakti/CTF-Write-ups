# Chunkies

### Challenge Description

We could only retrieve only this file from the machine, but looks like this is corrupted. Can you recover the file?

### Challenge Author

[v1Ru5](https://twitter.com/SrideviKrishn16)

### Short Writeup

The given PNG file is corrupted. Correct the header of the image. Fix IDAT and IEND chunks. On using the tool 'pngcheck' on the image, we see that there is a CRC error which can be directly corrected.

### Flag

shaktictf{Y4YyyyY_y0u_g0t_1T}
