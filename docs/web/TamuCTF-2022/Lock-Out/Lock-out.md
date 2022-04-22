# Lock Out
Solved by:
SriLakshmi Prathapan https://twitter.com/L0xm1_07
## Description
I seem to have locked myself out of my admin panel! Can you find a way back in for me?<br>
Do not connect with HTTPS, make sure to connect with HTTP<br>
Challenge Link: http://lockout.tamuctf.com
## Solution<br>
When we visit the link we can see the following page.<br>
![Image-1](https://github.com/L0xm1/CTF-Write-ups/blob/master/docs/web/TamuCTF-2022/Lock-Out/Image-1.png)
Lets click on the `login` button

When we click on the `login` button,we can see a login page with username and password.

![Image-2](https://github.com/L0xm1/CTF-Write-ups/blob/master/docs/web/TamuCTF-2022/Lock-Out/Image-2.png)

Since the goal of the challenge is to login as admin,I tried login using the `username:admin` and `password:admin`.I was not able to login and no error messages were displayed too.

To check if it was vulnerable to sql injection tried fuzzing with ‘,” ,\ etc but there weren’t any error messages .

Now I tried to intercept the request using burp with  `username:admin` and `password:admin`

![Image-3](https://github.com/L0xm1/CTF-Write-ups/blob/master/docs/web/TamuCTF-2022/Lock-Out/Image-3.png)

![Image-4](https://github.com/L0xm1/CTF-Write-ups/blob/master/docs/web/TamuCTF-2022/Lock-Out/Image-4.png)

From the above we can see that when we login ,the POST request is actually made to /admin.php.

But in the response we can see that the response comes as a `302` redirect that the browser will follow back to the login page before ever rendering the page to the user.

We can see a button `PrintFlag` on the admin page.

Now since the browser respond with a `302`  we could change the method to `GET` provide the `PrintFlag` as parameter 

`?PrintFlag=PrintFlag` where `PrintFlag` is the name as well as value of the button.

![Image-5](https://github.com/L0xm1/CTF-Write-ups/blob/master/docs/web/TamuCTF-2022/Lock-Out/Image-5.png)

And yes we got the flag `gigem{if_i_cant_wear_croc_martins_to_industry_night_then_im_not_going}`

**Flag:**`gigem{if_i_cant_wear_croc_martins_to_industry_night_then_im_not_going}`
