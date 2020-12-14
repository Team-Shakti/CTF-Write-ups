#EZ
**Challenge discription**
Lets try a beginners windows challenge!!!
**Author**:bl4ck_Widw

**Writeup:**
The file provided is a executable file , that can be reversed in windows OS
By using IDA decompilor in windows , you can get the peudocode of the challenge. Using that it will be very easy to reverse the program. All you have to do is reverse the functions and use the given string to find the input which will be the key. If the key you gave in is correct , use that key as the passcode in the executable ,to obtain the flag!

The solution script:
```
#include<stdio.h>
#include<string.h>
/* give the input as "lcZdl_Yoati+Xjn,lN!gGRdNR-R]H`=XjN,lo*+Iv" Shown in the challenge file and get the input to be used.*/
char* lol(char *input){
	int i;
	for(i=0;input[i]!='\0';i++){
		if(i>6&&i<=16){
			input[i]=input[i]--;
		}
		if(i>=0&&i<4){
			input[i]=input[i]++;
		}
		if(i>=4&&i<=6){
			input[i]=input[i]+3;
		}
		if(i<30&&i>16){
			input[i]=input[i]^4;
		}
		else
			input[i]=input[i]-5;

	}
	printf("%s\n",input);
	return input;

}
char* solo(char *soul){
	int l;
	for(l=0;soul[l]!='\0';l++){
		soul[l]=((soul[l]+5)^1);
	}
	return soul;
}
int main(){ 
	char input[100],ch;
	char output[100];
	printf("Enter passcode : \n");
	fgets(input,42,stdin);
	strcpy(output,solo(lol(input)));
	printf("Input should be :%s\n",output );

}
```

  **Flag**:shaktictf{n0_qu3sT1oN_iS_4_dUmB_qU3st10N}
