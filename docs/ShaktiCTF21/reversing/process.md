# pr0c3sses

On running the challenge it requires to enter a string of length < 10.
On opening up the binary we see a bunch of forks and compare statement with a string.

The challenge is divided in two parts. The first part targets even indexes of the input and the second part targets the odd indexes.

The goal is the choose such values from given switch cases as to get the string we get in the end to compare. 

Easiest and quickest way is to just create a fork tree.

Total no. of processes = 2^(no. of times fork called)

Let's take the first part.
First check the no. of processes being called. This can be done by checking the no. of `-` in the compare statement, because each process on finishing is ended with a `-`.
The no. of processes is 16. So we know the total no. of fork calls has to be 4.

Looking in switch cases which prints out what is being compared later. 

Then make a fork tree. The parent is printed out last. Hence the last `-` in the compare statement is the parent. This is because of the `wait(NULL)` which makes the parent wait until all child processes are completed. Trace back the path to get the required inputs.

Similarly do for the second part.

**Input given:** 23144105

**Flag:** shaktictf{p4r3nt_ch1ld_Ch17d_wut?_0n3_m0r3!}
