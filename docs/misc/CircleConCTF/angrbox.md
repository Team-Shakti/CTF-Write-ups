# CircleConCTF 21'

## angrbox

*Challenge Points : 261 Points*

## Description 

Write me a program that :
 - Takes 4 uppercase characters in argv
 - Verifies the 4 character key and returns 0 if correct
 - If I find the key , YOU LOSE

 `nc 35.194.4.79 7000`

 **Attachment**
 [angrbox.zip](https://github.com/Team-Shakti/CTF-Write-ups/blob/master/docs/misc/CircleConCTF/angrbox.zip)



## Writeup

**TL:DR**
- Pass on a C program to check the arguments against a predefined 4 character string
- Use path explosion so that angr would not be able to find a solution
    - In this case we just used a DLP problem in the check contraint

*(Interesting fact : We got the solve 3 min before the CTF ended in our first try . Was really exciting xD)*

### Challenge

After solving a PoW , the server asks for a C code that takes in a 4 character string as an argument.

We are to predefine a particular string in the code and check with the argument string. If both are equal the program returns a 0.

The server uses angr to guess the 4 character string in the passed C code within 2 min. 

```python
    print("[*] Write me a program that:")
    print("[*] - Takes 4 uppercase characters in argv")
    print("[*] - Verifies the 4 character key and returns 0 if correct")
    print("[*] - If I find the key, YOU LOSE")
    print("")
    print("[*] Enter your C code in hex:")
    src = bytes.fromhex(input())
    if len(src) > 2048:
        raise MyException("[-] Too long nitwit")

    print("[*] Compiling ...")
    filepath = compile(basename, src)

    print("[*] Solving (max 2 minutes) ...")
    key = solve_key(filepath)
```

You may find the angr script in solver.py and the session script in session.py

```python
    if key:
        print(f"[-] WoUlD yOu LoOk At ThIs KeY i FoUnD: {key}")
        raise MyException("[-] This code is WEAK SAUCE")
    else:
        print("[*] My solver couldn't find a key >:(")

    key = input("[*] Gimme ur key and I'll check it: ")
    if len(key.encode()) != 4:
        raise MyException("[-] The key needs to be 4 characters fool")
    if any(c not in string.ascii_uppercase for c in key):
        raise MyException("[-] The key can only contain UPPERCASE characters")

    success = check_key(filepath, key)
    if success:
        print("[*] WTF? YOUR KEY WORKS")
        print("[*] You are a crypto genius")
        flag = open("flag.txt").read().strip()
        print(f"[+] Here's your flag: {flag}")
    else:
        raise MyException("[-] ARE YOU KIDDING ME? THIS KEY DOESN'T EVEN WORK")
```

Our aim is to code a program which angr can't guess but returns 0 for the right input and the right input only.

### Approach

**1**

Our first thought was to make a script that takes a lot of time for the check.

There was a timing constraint of 2 min for angr in the config file. So we thought of putting a sleep(120) so that angr could not guess the value. This is what we tried :-

```c

#include<stdio.h>
#include<string.h>
#include<unistd.h>

int main(int argc,char *argv[])
{
    char str1[4]="DBCA";
    sleep(118);
    if(strcmp(argv[1],str1)==0)
        return 0;}

```

angr did find the wrong key however, it raises an exception and exits because it does not go to the else condition.

```python
    if key:
        print(f"[-] WoUlD yOu LoOk At ThIs KeY i FoUnD: {key}")
        raise MyException("[-] This code is WEAK SAUCE")
    else:
        print("[*] My solver couldn't find a key >:(")
```
So even if it did find the wrong key it does not recognize that the solution is wrong because it does not go to the else condition.

The only way left was to somehow make angr return the `None` for the key.

**2**

Our juniors , Pavani and Revathi came up with the idea to play around with the parameters in the angr.cfg file and so we did.

(4lex1)[https://github.com/sandrabeme] suggested that we use some functions that has a lot of memory utilisation , so that we could exceed angr's memory limitations and thus making it impossible for angr to solve the equation. Thus we starting trying to use memcmp and defining variables outside stack etc. But that just wasnt enough to exceed the memory limit.

Being a Crypto gal, the first thing that came to my mind was the Discrete Logarithm Problem. We framed the problem such that the first character of our string is the only solution to our DLP problem and if tried to brute-force, the memory utilisation would just grow exponentially. This was our final C code :

```c
int modpow(long long int x,long long int y,long long int n) {
  int ret = 1;
  for (; y; x = x * x % n, y >>= 1) {
    if (y & 1) {
      ret = ret * x % n;
    }
  }
  return ret;
}
 
int main(int argc,char *argv[]) {
  char *s = argv[1];
  char str[] = "ABCD";
  int x = (int)s[0] << 20;
  int g = 30;
  long long int p = 262717555471964216279378282832327568771;
  long long int y = 8520288065628959452076982415822625519;
  if(modpow(g,x,p) == y)
  {
    if(s[1] == 'B' && s[2] == 'C' && s[3] == 'D')
 return 0;
  }

}
```

Converting it into hex, and passing it to the server we got the flag.

![the-solution]()

### Flag
`CCC{p4th_3pl0s10n_4s_a_tr4pd00r_funct10n?_0r_d1d_y0u_ch33s3_1t}`

