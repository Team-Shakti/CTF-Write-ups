# Ador

### Challenge Description
Ada was born on 10 December 1815 not 12, identification change makes a difference

### Short Writeup
In the source code, you will find that name parameter is set to a default user, when we login with name as "admin", we get an idor and receive flag.
Payload=`?name=admin`

### Flag
shaktictf{f1r5t_c0mpu73r_pr0gr4mm3r}
