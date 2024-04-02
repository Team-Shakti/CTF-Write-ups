# Delicious

**Description**: How delicious!
**Author:  [Av4nth1ka](https://twitter.com/av4nth1ka)**

**Solution**: 

This was the most easiest challenge in the CTF. 
Intercept a request and take a look at the cookie.
Base64 decode the cookie and we will get {"admin":0}.
We can change the admin's value to 1 to make the user admin.
We can base64 encode this new JSON and send that as the cookie to get the flag.
Final Payload - eyJhZG1pbiI6MX0= ( Base64 decoded - {"admin":1} ).


Flag: `shaktictf{heyo_beginnerr_you_got_the_flag}`              