#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>

unsigned int num_dragons = 0;
int num_men = 3000;

void initialize()
{
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
	alarm(60);
}



void exit_function(int arg){
	if(arg == 0){
		return ;
	}
	else{
		exit(1);
	}
}

int use_dragons(){

	unsigned int dragons = 3;
	char inp[0x10];

	printf("\n\nYou currently have %d number of dragons.\n", dragons);
	if(dragons<= 0 || dragons > 3){
		puts("You either have too less or too many dragons!");
		exit_function(0);
	}
	else{
		printf("\nSay something in Valyrian: ");
		scanf("%10s", inp);
		getchar();
	
		printf("The dragons say: ");
		printf(inp);
		
	}

	return dragons;
}

void kings_landing(int *men, unsigned int *dragons){
	
	puts("1. Fight using men\n2. Fight using dragons\n");
	char ch;
	char inp[0x50];
	//fflush(stdout);
	scanf("%c", &ch);
	getchar();
	switch(ch){
		case '1':
			puts("No men left in the army! You cannot kill the knight king. ");
			*men = 0;
			break;
		case '2':
			if(*dragons<=0 || *dragons > 3){
				puts("You have too less or too many dragons! ");
				exit_function(0);
				break;
			}else{
				unsigned int num;
				printf("How many dragons would you like to use ?\n> ");
				scanf("%u", &num);
				if(num<=0 || num>3){
					puts("You only use dragons that you have");
					exit_function(0);
					break;
				}else{
					*dragons = *dragons - num;
					printf("%u dragon(s) have been used!\nAre you going to kill the white walkers ?\n> ", num);
					getchar();
					scanf("%50[^\n]s", inp);
					printf(inp);
					
					break;
				}
			}
		default:
			puts("Give a valid choice next time! ");
			exit_function(0);
			break;
		}
		
}

void white_walkers(int *men, unsigned int *dragons){
	puts("You are going to battle against an army of the dead! ");
	if((*men) != 30000 && (*dragons) != 200){
		puts("You do not have enough men or dragons to defeat the army of the dead"); 
		exit_function(0);
	}else{
		puts("Wonderful! You have defeated the army of the dead and have conquered King's Landing. You are the true ruler of the seven kingdoms. ");
		exit_function(1);
	}

}

void menu(){
printf("\n\n1. Use your dragons\n2. Capture Kings Landing\n3. Kill White Walkers\n\nYour choice: ");

}

int main(){

initialize();

// banner
puts("\n\n=================================================");
puts("|	Welcome to Game of Thrones (GOT)	|");
puts("=================================================\n\n");

puts("The goal is simple! You need to become the ruler of the seven kingdoms!");


char choice;

while(1){
	menu();
	choice = getchar();
	getchar();
	//fflush(stdin);

switch(choice){
	case '1':
		num_dragons = use_dragons();
		break;
	case '2':
		kings_landing(&num_men, &num_dragons);
		break;
	case '3':
		white_walkers(&num_men, &num_dragons);
		break;
	default:
		puts("Invalid choice!");
		exit_function(0);
		break;
	}
}

return 0;
}

