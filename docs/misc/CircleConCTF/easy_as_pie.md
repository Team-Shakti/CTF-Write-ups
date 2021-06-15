## CircleConCTF 21'

## Easy as Pie

*Challenge Points : 288 Points*


### Description 

An esoteric sketch, wouldn't you agree?

**Attachments** : [delicious.png](../delicious.png)

### Writeup

 - On performing a zsteg on the image we get the following 
 
    ![soln.png](https://github.com/aryaarun12/CTF-Write-ups/blob/master/docs/misc/CircleConCTF/soln-del.png?raw=true)
    
 - Writing it into a file and opening it we see that its a piet code 
 
    ![piet.png](https://github.com/aryaarun12/CTF-Write-ups/blob/master/docs/misc/CircleConCTF/new.png?raw=true)


 - Putting it into a [piet interpretor](https://www.bertnase.de/npiet/npiet-execute.php) we get the flag 
```CCC{n0th1ng_irr4ti0na1_4b0ut_p1}
```
