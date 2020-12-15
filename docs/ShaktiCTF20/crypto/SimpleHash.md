# SimpleHash

### Challenge Description

The 'Government Code and Cypher School' was founded  with a single purpose: that of breaking the German Enigma Code, which they thought to be non-reversible. But later it was broken by her and her team.

Hashes are said to be reversible too. Do you think you can reverse this hash though?

### Short writeup

Perform bruteforce attack to get the flag. Length of the flag is only 5 characters, making it easy to brute force.

```python
import string
import hashlib

x = "cb7a53dd721f4ca90b8fd3dbdabeda5a".decode("hex")
chars = list(string.ascii_lowercase + string.digits)

for i in chars:
	for j in chars:
		for k in chars:
			for a in chars:
				for b in chars:
					m = hashlib.md5()
					m.update("shaktictf{" + i+j+k+a+b + "}")
					if m.digest() == x:
						print "shaktictf{" + i+j+k+a+b + "}"
						break

```
### Challenge Author

[4lph4](https://twitter.com/__4lph4__)

### Flag

shaktictf{sup3r}
