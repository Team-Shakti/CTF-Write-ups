### Be Alert

***Description***: I made my first ever login page! Try to login.
<br>
**Author:  Ramya**

***Solution:***
When you visit the challenge link, we can see that `Something appears in /flag.html`. When we got to /flag.html, we can see a password field.
In the source code we can see the following javascipt code.
```
let word = "rg`jsh`clhm";
    let password = "";
    function chall(word) {
        for (let i=0; i<word.length;i++) {
            password += String.fromCharCode(word.charCodeAt(i) + 1);
        }
        return password
    }
```
When we run the above js code, we get the password as `shaktiadmin`. Submit the password in /flag.html and we get the flag.
Flag: `shaktictf{c0n9r4t5_u53r_hehe65445746}`


