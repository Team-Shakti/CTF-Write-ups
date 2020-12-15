# Findme

### Challenge Description
OSINT is popular these days. Kay hid your flag in a social networking website. Go get your flag. 


### Writeup
We have a file attached along with the challenge description. 
On opening the file we see the following:

---

Username: (2c1743a391305fbf367df8e4f069f9f9) + "x86" + (987bcab01b929eb2c07877b224215c92)

Username didn't work? Try and try. But don't come and "bash" me.

---

Description and the contents in the file suggest that the flag has something to do with social networking website. 
But using the username as it is won't work as the first and last parts are `MD5` hashes of the username. The word "bash" was simply used to hint that it's a "hash". 

Online tools like [crackstation](https://crackstation.net) can be used to crack the hashes. 
Upon cracking the hashes we get words `alpha` and `beta`
Joining them accordingly gives the username as: `alphax86beta`

Next part is finding the social networking site used. 
Here's where the description comes into use. Online OSINT tools can be used to find the social networking websites where an user account with the given username exists. 
[namecheckr](https://www.namecheckr.com) gives websites with the given username.
There are many social networking websites where an user account with the given username exists but Tumblr is the right one. Flag can be found in the description part. 

### Flag
shaktictf{H3y!!!0s1nt_pr0}

### Challenge Author
[4lph4](https://twitter.com/__4lph4__)