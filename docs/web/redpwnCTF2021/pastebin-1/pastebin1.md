# pastebin-1

## Description
In this challenge there is a pastebin service in which you can post your message and get a shareable link to your post. The admin bot will visit the URL you submit to it.
  
## Solution
The pastebin executes any javascript passed to it. XSS is possible. We can leverage this to access the admin bot's cookie when it visits our URL. Setup a webhook to receive the request. 

![index](../../images/3.png)

Submit the link to our paste to the admin bot

![index](../../images/4.png)

Javascript will try to load the image from the URL, passing cookie information along with it.

![index](../../images/5.png)

URL decode to get the flag.