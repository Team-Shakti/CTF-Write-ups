## Challenge Title: secRetS And seCReTs

### Challenge Description :
I think Sun Tzu forgot that greater the number of primes used, stronger would be the encryption.

### Difficulty Level
Easy

### Points
100

### Flag format 
shaktictf{...}

### Writeup
1. This challenge uses the chinese remainder theorem and RSA encryption to encrypt the flag. 
2. Making use of the crt function from sympy would give you the value of x.
3. From the final assert statemnt it can be understood that dviding the secret by x would give you the value of the modulus.
4. Upon using sympy's factorint you can deduce that the modulus is a square of a prime and so phi is calculated as prime*(prime-1).
5. The private key d can then be calculated as the inverse of e and phi. 
6. The plain text can be calculated using the formula pt=(ct^d)%n and that on converting to bytes and decoding gives us the flag.

### Flag
shaktictf{w0w_you_kn0w_h0w_RSA_&_CRT_w0rks_!}

### Author
Rees





