## Challenge Name: Ping-Pong
### Author :[L0xm1](https://twitter.com/L0xm1_07)
## Challenge Description
A simple ping service .Is it vulnerable?
## Writeup
When you visit the challenge link ,we are welcomed with **"Enter the hostname to ping  Example: /ping?address=google.com"**

When we visit the /ping endpoint with ?address={hostname to ping}and  give **/ping?address=google.com** ,we get the ping response of google.com.

Here if we give **/ping?address=google.com|ls** we can get the contents in the directory i.e **(app.py flag.txt templates)**

When we try  **/ping?address=google.com|cat flag.txt**  it throws out an error **Not Allowed** which indicates cat is blacklisted.

We can use head,more,tail etc to read the flag.

When we give /ping?address=google.com|head flag.txt we get the flag.

## FLAG
**shaktictf{c0mm4nd_1nj3cti0n_iz_3asy_right??}**
