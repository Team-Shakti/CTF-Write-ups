# Twisted_Calc

### Description

Scientists are trying to figure out how this calculator works. They are essentially trying to crack the algorithm. Can you help them with it?

**Author: [k1n0r4](https://twitter.com/k1n0r4)
Difficulty level: Hard
Points: 500
Category: Reverse Engineering**

###  Solution

The given file is an ELF 64-Bit Executable.

##### What all is happening with the input?

- The input is taken and xorred with a predefined array of length 50 byte by byte. This indicates that the flag length is 50.
- Later it goes through a `check` function which contains constraints for the manipulated input.
- Next, a digital signal (in form of 1's and 0's) is declared.

![image](https://imgur.com/eYFIpGP.png)


- The xorred input is used to determine what operations will be performed on the given signal via the `applySignalProcessing` function.

![image](https://imgur.com/Yf2qCpn.png)

- For every 5th index of the input, the state of the signal is being checked under the `second_check` function.

#### Towards the flag

Analysing the `applySignalProcessing` function indicates the use of 10 operations, hence there are only 10 possible elements of v10 array. 

For each batch of 5 elements of v10 array, there are 3 checks given to us in `check` function and a final signal state check in `second_check` function.

```clike!
# Checks for the first batch of 5 elements

if ( (a1[3] ^ a1[2] ^ a1[1] ^ *a1 ^ a1[4]) != 44 )
    exit(0);
if ( *a1 != 32 )
    exit(0);
if ( a1[4] != 47 )
    exit(0);
```


Utilising these constraints and the fact that there are only 10 possible values, we can brute and get the values.

One simple way to confirm which is the correct value could be by xorring the obtained values with the predefined array in step 1 and see which of the string makes sense or is readable.

```clike!
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int applySignalProcessing(int digitalSignal, int operation, int parameter) {

    switch (operation) {
        case 20: 
            return digitalSignal;

        case 23: 
            return digitalSignal * 8;

        case 26: 
            return digitalSignal + (parameter*3);

        case 29: 
            if(digitalSignal > 1000)
                return digitalSignal;
            else
                return digitalSignal * parameter * parameter;

        case 32: 
            return digitalSignal ^ parameter;

        case 35: 
            if(digitalSignal > 1000000)
                return digitalSignal / 1000;

        case 38: 
            if(digitalSignal > parameter)
                return digitalSignal - parameter;
            else
                return digitalSignal;

        case 41: 
            if(digitalSignal > 10000)
                return digitalSignal;
            else
                return digitalSignal * parameter;

        case 44: 
            return digitalSignal * 2 ;

        case 47: 
            return digitalSignal + parameter;


        default:
            return 0; 
    }
}

int main()
{
    int a1[50] = {0};
    a1[0] = 0x20;
    a1[5] = 32;
    a1[10] = 23;
    a1[15] = 41;
    a1[20] = 35;
    a1[25] = 26;
    a1[30] = 26;
    a1[35] = 29;
    a1[40] = 26;
    a1[45] = 38;
    a1[4] = 0x2F;
    a1[9] = 26;
    a1[14] = 47;
    a1[19] = 47;
    a1[24] = 41;
    a1[29] = 29;
    a1[34] = 44;
    a1[39] = 29;
    a1[44] = 20;
    a1[49] = 26;

    int signal[50] = {1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0};
    int oper[10] = {20, 23, 26, 29, 32, 35, 38, 41, 44, 47};
    int check[10] = {44, 31, 29, 20, 29, 42, 31, 47, 43, 42};
    int final[50] = {44, 40, 44, 44, 44, 40, 40, 44, 40, 44, 40, 44, 40, 44, 40, 44, 40, 44, 44, 44, 40, 40, 40, 40, 44, 44, 40, 40, 44, 40, 44, 44, 40, 44, 44, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40};

        for(int a = 0; a<10; a++)
        {
            for(int b = 0; b<10; b++)
            {
                for(int c = 0;c<10;c++)
                {
                    int signal[50] = {1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0};

                    if((a1[0]^oper[a]^oper[b]^oper[c]^a1[4]) == 44)
                    {
                        int ope[5] = {a1[0], oper[a], oper[b], oper[c], a1[4]};
                        int res[3] = {oper[a], oper[b], oper[c]};
                        for( int i = 0;i<5;i++)
                        {
                            for(int j=0;j<50;j++){
                                signal[j] = applySignalProcessing(signal[j], ope[i], 10);
                            }
                        }
                        int c = 1;
                        for(int k =0;k<50;k++){
                            if(final[k] != signal[k]){
                                c = 0;
                            }
                        }
                        if(c==1){
                            printf("\nSolution found: %d %d %d\n\n", res[0], res[1], res[2]);                            
                            break;
                        }
                    }
                }
            }
        }
}
```

Output:

`Solution found: 44 44 35`

The given solution, on xorring back gives the result as `shakt`, which is the starting 5 bytes of the flag format.

Similarly, all the 10 batches of elements can be retrieved and formed into the flag.

### Flag

`shaktictf{3l3ctr0n1cs_s0m3t1m3s_1s_p41n_735294758}`