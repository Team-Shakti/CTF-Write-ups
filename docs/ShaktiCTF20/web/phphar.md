# PHPhar

### Challenge Description

Explaining the Analytical Engine's function was a difficult task, bypass the basic php to see what she tried to explain

### Short Writeup
bypass first function by giving an exponential value, second check by giving a decimal value with total 13 letters and the value before the . being 1337, for third check use array indice manipulation of the two parameters being checked to bypass the sha1 check, for the fourth check, provide a md4 with 0e followed by xxxx which would be a loose comparison with 0e and for the last check use an array to bypass the strcmp() 
Payload --> `flag0=9e9&secret=1337.12345678&a[0]=asd&b[1]=dsf&md4=0e251288019&abc[]=sdff`

### Flag

shaktictf{An4ly71c4l_Eng1n3!=D1ff3r3nc3_Eng1n3}
