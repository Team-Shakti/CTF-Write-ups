# Speedrun 3
## Description
* [link](http://challenges.ctfd.io:30043/)

## Solution
* First, we enter the site and randomly fill in the input
* We then refresh it and see {"admin":false,"name":"asd"}
* We also note that a cookie, named authtoken was created, with the value eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6ZmFsc2UsIm5hbWUiOiJhc2QifQ.i9II9riAxP5OSQrVDrRX2dOnNaJI_K4Vk9FED-ADuVs
* We play around with the cookie by deleting half of it, and was greeted with an error
* Fatal error: Uncaught UnexpectedValueException: Wrong number of segments in /var/www/html/index.php:84 Stack trace: #0 /var/www/html/index.php(531):
* Firebase\JWT\JWT::decode('eyJ0eXAiOiJKV1Q...', '82a59879a507', Array) #1 {main} thrown in /var/www/html/index.php on line 84

### JWT 
* When we google JWT decoder we get the link [link](https://jwt.io/)
* We find that the format for the code is JWT::decode($payload, JWK::parseKeySet($jwks), $supportedAlgorithm);
* Hence, we input the 256-bit-secret as 82a59879a507
* Now, it is verified

### Getting the flag
* We use the tool to change admin to true, and get eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6dHJ1ZSwibmFtZSI6ImFzZCJ9.YTbnlIIllCx5UyHp4N-M1f00hDl5erOGmq2V17N8RKg

### Flag is:
* > UDCTF{st00p1d_PHP_err0r_mess4ges}


