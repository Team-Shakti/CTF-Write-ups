# APLab:Statistics HSCTF

## Description

A fun Java RE challenge from HSCTF-2020

The given file was a .class file which had to be converted to a .java file using any online converters or tools like jadx.Once you get the .java file I was initially not able to convert the java code due to an invoke to call a direct java bytecode for which I simply changed the line to an equivalent funtion that is simply toString to fix that.

Thereafter we figured that the code was performing certain manipulations on the input and would simply check between the two strings. But the catch was where there was a sortof non reversible bubble sort kind of algorithm which picked up the two smallest values in the string and pushed them to the end of the string. And due to that a few charecters of the flag had to be guessed.
However the following is the script that we used to solve the challenge.

## Solution

'''java

import java.util.Scanner;
public class statistics
{
    public static void main(final String[] args) {


        int[] arr =  {102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        // checkstring="qtqnhuyj{fjw{rwhswzppfnfrz|qndfktceyba"
        String com = "fqntqdhuyj{fjw{rwhswzppfnbrz|qncfktaey";
        String guess = "abcdefghijklmnopqrstuvwxyz{_}|";
        System.out.print("f");
        for (int i = 1 ; i<com.length() ; i ++){
            char st = com.charAt(i);
            for (int k = 0;k< guess.length();k++){
                if (arr[i - 1] % 2 == 0) {
                    arr[i] = guess.charAt(k) + (arr[i - 1] - 97);
                }
                else {
                    arr[i] = guess.charAt(k) - (arr[i - 1] - 97);
                }
                arr[i] = (arr[i] - 97 + 29)%29 + 97;
                if((char)arr[i] == st){
                    System.out.print(guess.charAt(k));
                   break;
                    }
            //System.out.println((char)arr[i]);
        }}
    }
}

'''

`Output: flag{tenpercentofallstatirqicsashfake}`

We had to perform several tries to finally guess the few last charecters we needed to complete the flag. But it was worth!
<p align="center">

<img width="200" height="100" src="../../images/stat.png">

</p>
`Flag: flag{tenpercentofallstatitoicsarefake}`
