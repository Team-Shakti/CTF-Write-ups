## Challenge Title: r3deem_r4Nd0m

### Challenge Description :
You know, everything is fair in CTFs and competition.

### Difficulty Level
Hard

### Points
300

### Flag format 
shaktictf{...}

### Writeup
1. This challenge first computes the hashing function of flag to produce the signature for system. chinese remainder theorem and RSA encryption to encrypt the flag. 
2. The final signature is computed by using CRT. Check if that final signature equals the hash value calculated in step 1.
3. The attack is to modify the signature of each prime number and recalculate the final signature.
4. compute gcd(S^e − H, N ) to get product of other two primes. 
5. Calculate gcd(S^e − H, N) for three times , where you are modifying `Sp`,`Sq`,`Sr` and calculating S.
6. Find gcd among that results to get p,q,r. 

### Flag
`shaktictf{rand0m_cr4z7_p3rs0n_aLw4ys_tries_cr7pt0_a7de4873ca0f9f697f1d2c09004f33dc1ad98b64}`

### Author
Pavani





