# Hack

##### Challenge Author: bl4ck_Widw
##### Points : 50
##### Description 
Lets compare!

### Writeup

This challenge is a fairly simple one but a bit tricky for beginners . 
The challenge emphasises on string compare . The input gets compared with a small part of an array already provided. The player just have to figure out which part gets compared with to find the flag.

Solution script:
```
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int v2[30]={89,51,115,95,95,72,52,99,75,95,116,72,51,95,77,48,48,110,95,95,33,33,95,72};
int main(){
	char v1[16];
	int j;
	//shaktictf{__H4cK_tH3_M00n_}
	for(j=0;j<16;j++){
		v1[j]=(char)v2[j+3];
	}
	v1[j]='\0';
	printf("shaktictf{%s}\n",v1);
}
```

```
Flag:shaktictf{__H4cK_tH3_M00n_}
```

