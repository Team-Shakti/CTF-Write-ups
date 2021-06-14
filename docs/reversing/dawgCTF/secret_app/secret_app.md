# DawgCTF 2021

## Secret app(Reversing)

## Challenge description

![Description](https://github.com/revathi2001/dawgCTF-writeup/blob/main/Selection_120.png)

[Challenge file](https://github.com/revathi2001/dawgCTF-writeup/blob/main/secret_app.exe)

- Opening the file in ghidra and going to defined strings from window menu, we can find the strings ```Please enter username``` and ```Please enter password```.

- On going to corresponding functions username is ```not_username``` and password is ```not_password```.

- Going to function just before printing of flag, there our input is getting compared with result of hexdata xored with 0x78. Using simple python code we get flag.
```
hexa=["3c","19","0f","1f","3b","2c","3e","03","4c","08","08","27","0b","0d","08","4b","0a","27","4d","4b","1b","0a","1d","0c","05"]
for i in hexa:
	print(chr(int(i,16)^120),end="")
```

## Flag

``` DawgCTF{4pp_sup3r_53cret}```
