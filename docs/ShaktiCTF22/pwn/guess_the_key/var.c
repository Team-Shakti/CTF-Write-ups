#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(){
    printf("Guess the correct key to win!\n");
	int para = 0xdeadbeef;
	char key[48];
	printf("Enter the key: ");
	gets(key);	
	if(para == 0xcafebabe){
		system("cat flag.txt");
	}
	else{
		printf("Wrong Key\n");
        printf("Try again!\n");
	}
}
int main(int argc, char* argv[]){
	setvbuf(stdout,NULL,_IONBF,0);
	func();
	return 0;
}