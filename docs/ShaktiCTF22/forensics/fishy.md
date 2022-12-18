# Fishy File 

### Challenge Description

We have got a confidential file from a criminal's system but we're unable to retrieve anything from the file. Can you help us?

### Challenge Author

[v1Ru5](https://twitter.com/SrideviKrishn16)

### Writeup

The given file is a pdf file where the bytes are reversed. The first step is to change the file extension. Let's now write a script to get the actual pdf file.

```
f1 = open("flag.pdf", "w")
with open("shakti.pdf", "r") as myfile:
    data = myfile.read()
rev = data[::-1]
f1.write(rev)
f1.close()
```
Binwalk command shows us that a pdf and an image file are embedded in flag.pdf. Let's extract the files using the following command.

```
foremost flag.pdf
```

The extracted pdf file is a rabbit hole. We only get a fake flag. So let's now focus on the png file.

The extracted png file is corrupted. Fix IHDR, IDAT and IEND chunks to get the flag.

### Flag

shaktictf{Y0Uuu_G0t_Th1Ss5}
