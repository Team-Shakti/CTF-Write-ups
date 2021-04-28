# Ciphper

Solved by: Sowmya (@__4lph4\_\_)

Description:
```
Background story: this code was once used on a REAL site to encrypt REAL data. Thankfully, this code is no longer being used and has not for a long time.

A long time ago, one of the sites I was building needed to store some some potentially sensitive data. I did not know how to use any proper encryption techniques, so I wrote my own symmetric cipher.

The encrypted content in output.bin is a well-known, olde English quote in lowercase ASCII alphabetic characters. No punctuation; just letters and spaces.

The flag is key to understanding this message.
```
Take a look at the challenge script for better understanding: 
```php
<?php

function secure_crypt($str, $key) {
  if (!$key) {
    return $str;
  }

  if (strlen($key) < 8) {
    exit("key error");
  }

  $n = strlen($key) < 32 ? strlen($key) : 32;

  for ($i = 0; $i < strlen($str); $i++) {
    $str[$i] = chr(ord($str[$i]) ^ (ord($key[$i % $n]) & 0x1F));
  }

  return $str;
}
```

Output: 
```
sf'gh;k}.zqf/xc>{j5fvnc.wp2mxq/lrltqdtj/y|{fgi~>mff2p`ub{q2p~4{ub)jlc${a4mgijil9{}w>|{gpda9qzk=f{ujzh$`h4qg{~my|``a>ix|jv||0{}=sf'qlpa/ofsa/mkpaff>n7}{b2vv4{oh|eihh$n`p>pv,cni`f{ph7kpg2mxqb
```

Through the code given, it can be understood that this is a classical multi byte xor with a small modification. Observe the line: 
`
$str[$i] = chr(ord($str[$i]) ^ (ord($key[$i % $n]) & 0x1F));
`
Other than the `XOR` operation there is an extra `AND` operation. On some observation I found that this AND operation converts `ord(a) to 1 , ord(b) to 2 , ord(c) to 3 ..`
Next, I used the flag format `'gigem{'` to find the first few characters of the quote. After getting the quote characters, some googling helped me in finding the correct quote which I used for finding the key. Key found is random bytes because of `&0x1f`. It was further decoded to get the flag bytes. 

Doing all this gave me the flag as: gigem{dont\^roll\^your\^own\^crypto} which wasn't correct on submission. Finally, I understood that ^ and ~ give the same output due to the `AND` operation. So after changing ^ characters to ~ gave me the flag. 

Flag: `gigem{dont~roll~your~own~crypto}` 