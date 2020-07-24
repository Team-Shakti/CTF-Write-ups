#APLab:Computer Science principle HSCTF

## Description

A java RE challenge from HSCTF 2020

The challenge gives a simple java code ,which basically takes in an input of length 18,
```
if (inp.length()!=18) {
            System.out.println("Your input is incorrect.");
            System.exit(0)
}
```
Convert it to a string through different functions 
```
inp=shift2(shift(inp));

```

where shift2():

```
     public static String shift2(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)+ Integer.toString((int)input.charAt(i)).length());
        }
        System.out.println(ret);
        return ret;
    }
```
Shift():
```
    public static String shift(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)-i);
        }
        System.out.println(ret);
        return ret;
    }
```
and checks if inp is the string given.:
```
if (inp.equals("inagzgkpm)Wl&Tg&io")) {
         System.out.println("Correct. Your input is the flag.");
         }
         else {
             System.out.println("Your input is incorrect.");
         }
```
So all the program needed was to reverse it to get the input they are asking for

Hence
```
import java.util.Scanner;
public class ComputerSciencePrinciples
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.nextLine();
        if (inp.length()!=18) {
            System.out.println("Your input is incorrect.");
            System.exit(0);
        }
        String x=shift2(inp);
        String y=shift(x);

        System.out.println(inp);
    }
    public static String shift(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)+i);                        
        }
        System.out.println(ret);
        return ret;
    }
    public static String shift2(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)-Integer.toString((int)input.charAt(i)).length());
        }
        System.out.println(ret);
        return ret;
    }
}
```
Where if input is given as:"inagzgkpm)Wl&Tg&io"
Give:
 flag{intr0_t0_r3v}

