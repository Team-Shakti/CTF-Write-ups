# include<stdio.h>
#include<stdlib.h>
#include <unistd.h>
#include <sys/syscall.h>

void __register_tm_clones(){
__asm__("mov %r10, %rbx\nret\n"
	"xor %rax, %rax\nret\n"
	"xor %rbx, %rax\nret\n"
	"xor %rbx, %rbx\nret\n"
	"xor %rbx, %rdx\nret\n"
	"xor %rdx, %rdx\nret\n"
	"xor %r10, %r10\nret\n"
	"xor %r12, %r10\nret\n"
	"movq %r10, (%rdx)\nret\n"
	"syscall\n");
}

int main(){

setvbuf(stdout,NULL,_IONBF,0);

system("echo 'The fisherman is trying to untangle his fishing knots. If you could help him with it, it would be great!\n'");
char help[0x10];
fgets(help, 0x149, stdin);

system("echo 'Ok bye!\n'");

return 0;

}
