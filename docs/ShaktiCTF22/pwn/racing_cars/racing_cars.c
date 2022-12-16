#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

void initialize()
{
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
	alarm(60);
}

struct node{
	int id;
	char buffer[32];
	struct node* next;
	struct node* prev;
};

int bad(){
	printf("\n\nSorry you lost the race! Try again later :)\n");
	exit(0);
}

void (*function_pointer)()= &bad;
char array[50]={0};
struct node *head=NULL;

int insert(int id){
	struct node *temp = malloc(sizeof(struct node));
	temp->next = NULL;
	temp->id = id;
	if(head==NULL){
		head = temp;
		head->prev = NULL;
		return 1;
	}
	struct node *iter = head;
	while(iter->next != NULL){
		iter = iter->next;
	}
	iter->next = temp;
	temp->prev = iter;
	return 1;
}

int get_name(int id){
	struct node *temp = head;
	while(temp->id != id && temp->next != NULL)
		temp = temp->next;
	if(temp==NULL)
		return 0;
	fgets(temp->buffer,0x100,stdin);
	return 0;
}

int delete(int id){
	struct node *temp = head;
	while(temp->id != id && temp->next != NULL)
		temp = temp->next;
	if(temp==NULL)
		return 0;
	if(temp->next == NULL)
		temp->prev->next = NULL;
	if(temp->prev == NULL)
		temp->next->prev = NULL;
	if(temp->next != NULL && temp->prev != NULL){
		temp->prev->next = temp->next;
		temp->next->prev = temp->prev;
	}
	free(temp);
	return 0;
}

int main(){
	
	time_t t1; // declare time variable 
	srand((unsigned)time(&t1)); 
	
	initialize();
	int arr[0x5];
	int j = 0;
	int i=0;
	
	for(j=0; j<5; j++){
		arr[j] = rand();
	}
	
	puts("==================================");
	puts("    Welcome to the Incredibles    ");	
	puts("==================================");
	
	puts("To compete in the race you need to first buy a car!\n\nThe price of each car is given below: ");
	printf("1. Lexus RC F GT3 (Emil Frey Racing):	%d\n", arr[0]);
	printf("2. Porsche 911 RSR (991): 		%d\n", arr[1]);
	printf("3. Mercedes-AMG GT3:			%d\n", arr[2]);
	printf("4. Toyota FT-1 Vision Gran Turismo:	%d\n", arr[3]);
	printf("5. Renault Sport R.S.01 GT3:		%d\n", arr[4]);
	printf("\nChoose your car: ");
	
	fgets(array,50,stdin);
	
	for(i=0;i<3;i++){
		
		insert(i);
	}
	
	printf("\nEnter your details before you begin the race\nName: ");
	get_name(0);
	
	printf("\nOccupation: ");
	get_name(2);
	
	printf("\nAddress: ");
	get_name(1);
	
	delete(1);
	
	//printf("%d\n",sizeof(struct node));
	(*function_pointer)();
	//printf("%d\n",sizeof(struct node));
	return 0;
}
