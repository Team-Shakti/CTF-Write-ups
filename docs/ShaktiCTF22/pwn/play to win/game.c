#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void winfunc()
{
    printf("Ah well, you did win afterall.\n");
    printf("I guess congratlations are in order.\n");
}
void game()
{
    printf("You think you can do this?\n");
    printf("I don't think so.\n");
    char str[10];
    char s[2];
    int win;
    int check = 0;
    int count=0;
    while (check!=1)
    {
        printf("Add the word:");
        gets(str);
        count+=strlen(str);
        if (count==10000)
        {
            check=1;
            win=1;
            break;
        }
        printf("Do you want to continue?\n");
        printf("Yes or No [y/n]:");
        scanf("%s", s);
        getchar();
        if (s[0]=='y' || s[0]=='Y')
        {
            check=0;
            continue;
        }
        else if (s[0]=='n' || s[0]=='N')
        {
            check=1;
        }
        else
        {
            printf("Wrong input.\n");
        }
        
    }
    if (win==1)
    {
        winfunc();
        exit(0);
    }
}
int reallywin()
{
    printf("I may have underestimated you\n");
    printf("You win!\n");
    system("cat flag.txt");
    exit(0);
}
int main()
{
    setvbuf(stdout,NULL,_IONBF,0);
    game();
    return 0;
}