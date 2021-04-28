# Recovery 

*Challenge points* : 300

## Description

I needed to copy a flag from my home computer to the mainframe at work, so I used a floppy drive. It looks like a few bytes in the file got corrupted, so I deleted the file thinking it would be fine, but my friend says that’s not enough to prevent hackers from recovering the data.

## Solution

I used Autopsy to recover the delete file which was a GIF file f0000000.gif but it was corrupted. From various resources I learnt about GIF file format and tried to interchange the height and width of the image data of the GIF file and got the flag.

Flag : `gigem{0u7_0f_516h7_0u7_0f_m1nd}`







