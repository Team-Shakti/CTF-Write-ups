# Baby_Rust

Analysing it dynamically gets us to xoring instructions:

```
d ="adhmp`badO|sL}JuvvFmiui{@IO}QQVR"
k=0
for i in d:
	s=s+chr(ord(i)^(7+k))
	k=k+1
print(s)
#flag{look_ma_i_can_write_in_rust}
```
