# Gilberto’s Brother-OSINT 

## Description 

I made a mistake while making a writeup for a challenge from METACTF 2021. Can you find it?

## Solution:

On unzipping the given zip file, we find readme file and a `.git` folder

The README file has a python script

Using git grep and git rev-list revealed the flag we are looking for

`git grep 'gigem' $(git rev-list --all)`
![](../assests/4.png)
## Flag 

gigem{b3_car3ful_b3for3_y0u_c0mmit}



