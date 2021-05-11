# BlueHens CTF 
## CTFVC - Web
When we first visit the url we see a PHP code written

<?php if (isset($\_GET\['file'\])){ $file \= $\_GET\['file'\];  
    if (strpos($file, "..") === false){  
      include(\_\_DIR\_\_ . $file);  
    }  
  } //Locked down with version control waddup echo highlight\_file(\_\_FILE\_\_, true);  
?>

It is passing a file as a query parameter and might be a directory traveral attack.So this must be an exposed git repository attack.

Using https://github.com/internetwache/GitTools Dumper and Extractor scripts we can  extract the one commit, and looking at the metadata we are not given access to the directory "1a2220dd8c13c32e" 
in the version control system.
VC stands for version control

On passing this in the url ?file=/1a2220dd8c13c32e/flag.txt

we get the flag
UDCTF{h4h4_suck3rs_i_t0tally_l0ck3d_th1s_down}




