# Shaktictf 22 write-ups
## pyjails - level0,level1 and endgame
### level0
Description:

Solve level0 of the pyjail series!

Note: The server is running on Ubuntu 22.04.

Flag format: shakti{}

Author: Claire de lune

### Intended solution
The intended solution is to use the `__builtins__` module to access the `import` function and read the flag.
Running the file gives us the following output:

![](https://i.imgur.com/S4Jxynu.png)

On trying to import the os module, we get the following error:

![](https://i.imgur.com/ET1ikPk.png)

Which means the import function has been blocked somehow.
So we try to access the `__builtins__` module and import the os module from there.
#### Exploit
```python
 __builtins__.__import__('os').system('cat flag.txt')
 ```
This gives us the flag: `shakti{7h47_w45_7Un!3a36rgjsk9}`
 
### level1
Description:

Solve level1 of the pyjail series!

Note: The server is running on Ubuntu 22.04.

Flag format: shakti{}

Author: Claire de lune

### Intended solution
The intended solution is to use globals() to find the `__builtins__` module and access the `import` function to read the flag.
Running the file gives us the following output:

![](https://i.imgur.com/a0KytYg.png)

On trying to run the last exploit, we get the following error:

![](https://i.imgur.com/oO3eyPR.png)

Which means the `__builtins__` module has been blocked somehow.
So we try to access the `__builtins__` module using globals().Running globals() gives us the following output:

![](https://i.imgur.com/PtoKmTV.png)

We can see that the `__builtins__.__import__` module is present in the globals() dictionary.
So we try to import the os module from there.
#### Exploit
```python
we_need_you_alive.('os').system('cat flag.txt')
 ```
This displays the message:

![](https://i.imgur.com/j1sojOZ.png)

 The flag is : `shakti{7h47_W45_4_Cl053_C4ll!!!}`
### endgame
Description:

Solve endgame of the pyjail series!

Note: The server is running on Ubuntu 22.04.

Flag format: shakti{}

Author: Claire de lune

### Intended solution
The intended solution is to use globals() to find the `__builtins__` module and access the `import os` function to read the flag.Also the exec function has been blocked.
Running the file gives us the following output:

![](https://i.imgur.com/AT7ASIx.png)

Let's try using the helpline:

![](https://i.imgur.com/SAfMEP2.png)

So the helpline id is the password in the message that was displayed at the end of the last game. The helpline is basically globals() function which shows the banned list containing the functions: print, exec, eval,read,open and globals(). It also shows the os module saved as 'sos' and exec function saved as 'beat_the_master'.

#### Exploit
```python=
beat_the_master('sos.system("cat flag.txt")')
```
This displays the message:

![](https://i.imgur.com/wgr4eD0.png)

The flag is: `shakti{H0w_D0_y0u_L1k3_35c4p3_r00m5_n0W?}`
