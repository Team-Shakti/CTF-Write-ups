# L0g1n F4il3d

***Description***: I made my first ever login page! Try to login.
**Author:  [Av4nth1ka](https://twitter.com/AvanthikaAnand1?t=U4sSUyEOg7VPPZ_0S6LybQ&s=09)**

***Solution***: 

This is a very very basic SQL injection challenge. First of all we have a login page.

When we try to login with some username and password, we get the message as “wrong credentials”. When we get a login page the first thing we look for is whether the page is vulnerable to SQL injection or not. 

So we can try giving a very basic sql injection payload.

payload: ` ‘ or 1=1 — `

When we give the above query to the username or password field we get a message as follows.
 
 **Hey '' or 1=1 --'! Here is your flag: '('admin', 'shaktictf{s1mpl3_sql_inject1on_ehehhehe564321345}')'.**

YEAHH! We got the flag!! From the above message we can understand that admin’s password was the flag. 

Flag: `shaktictf{s1mpl3_sql_inject1on_ehehhehe564321345}`