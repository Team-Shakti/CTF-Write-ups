# Phase Stream 4

Solved by: Sowmya (@__4lph4\_\_)

This is the last set of the Phase Stream challenges. This challenge involves the `cribdragging` approach.

Here is the challenge script: 
```python
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

KEY = os.urandom(16)


def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128))
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()


with open('test_quote.txt', 'rb') as f:
    test_quote = f.read().strip()
print(encrypt(test_quote))

with open('flag.txt', 'rb') as f:
    flag = f.read().strip()
print(encrypt(flag))

```

Output: 
```
2d0fb3a56aa66e1e44cffc97f3a2e030feab144124e73c76d5d22f6ce01c46e73a50b0edc1a2bd243f9578b745438b00720870e3118194cbb438149e3cc9c0844d640ecdb1e71754c24bf43bf3fd0f9719f74c7179b6816e687fa576abad1955
2767868b7ebb7f4c42cfffa6ffbfb03bf3b8097936ae3c76ef803d76e11546947157bcea9599f826338807b55655a05666446df20c8e9387b004129e10d18e9f526f71cabcf21b48965ae36fcfee1e820cf1076f65
```

Points to be noted: 
```
1. We are given 2 ciphertexts:
    1. Ciphertext of the flag
    2. Ciphertext of the quote
2. We know the flag format "CHTB{"
3. Key is reused in AES-CTR which reduces its strength to that of XOR
```

We first XOR both the ciphertexts to remove the effect of the key. Now we use the flag format `CHTB{` to get the initial part of the quote. Through some guessing and googling we have to figure out the quote little by little. Challenge name is also helpful in guessing some part of the flag.

Flag: `CHTB{stream_ciphers_with_reused_keystreams_are_vulnerable_to_known_plaintext_attacks}`

