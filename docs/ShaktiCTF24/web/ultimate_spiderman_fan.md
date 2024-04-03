# Ultimate Spiderman Fan


**Description**
  <br>
  Welcome to the Spider-Man Merch Portal Challenge! Your mission, should you choose to accept it, is to harness your web-slinging skills and become the ultimate Spider-Fan. Are you ready to prove your worth and claim your rightful place among the elite Spider-Fans? 
<br>

**Author:  [L0xm1](https://twitter.com/L0xm1_07)**

**Solution**
<br> 

When we visit the challenge link, we are greeted with a Spiderman Merch Shopping Portal where we can purchase Spiderman merchandise. Among the offerings is a "Spider Surprise" priced at $5000, exclusively available to ultimate fans. Upon purchasing any Spiderman merch, a cookie named *shopping_token* is set, containing a JWT token. Let's proceed to jwt.io to decode this token.

Our objective is to get the Spider Surprise priced at $5000. To achieve this, we will modify the amount in the JWT token to 5000 and change the algorithm to None. Subsequently, we will update the *shopping_token* cookie with the updated JWT *eyJhbGciOiJOb25lIiwidHlwIjoiSldUIn0.eyJhbW91bnQiOjUwMDB9.StIPl3HpNpEElSOleho_cOlC2YLRHewcpLI2xkG42AQ*. This challenge is based on exploiting the JWT-None algorithm vulnerability.



*Flag: `shaktictf{Y0u_4re_th3_ult1mat3_f4n}`*  

