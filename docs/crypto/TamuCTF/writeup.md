# TamuCTF

## pwngen

Author : [ph03n1x](https://github.com/meenakshisl)

**TL;DR**
1. Given the equation of a Linear congruential generator (LCG) and the previous password generated using it
2. Use z3 to find the seed with the given contraints.
3. Find the seed and get the next password from it.


# Challenge

*Challenge points* : 150
*Challenge solves* : 10

#Description

(*not the exact description*)

It has been found that a set of passwords have been generated using the given script.We have reason to believe that they generated a set of passwords at the same time using a custom password generation program and that their previous password was `ElxFr9)F`. Send the next password at `openssl s_client -connect tamuctf.com:443 -servername pwgen -quiet`.

Files : [main.rs]()