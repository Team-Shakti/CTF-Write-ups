# Grocery List

## Writeup

This challenge was based on an esolang programming language(Grocery List) as the challenge name suggested. 
First decode the Base64 string given:

```Reverse GroceryPlace

vichyssoise             
mango                   
vermouth
zucotto
sandwich
lamb
veal
yogurt
vermicelli
zucchini
salmon
fennel seeds
ice cream
carrots
unagi
inca berries
cabbage
upma
grapes
naan
apples
bananas
almonds
basil
fenugreek
potatoes
pie
soy beans
eggs
tunafish

Find the input to the following output.
OUTPUT: 4cum77itQdKy4r7c~rm5u05plN```

After decoding, it says that some input is passed to the grocery list given and we receive an output for that. This suggests that this talks about some kind of a program. 
On googling we find an esolang [Grocery List](https://esolangs.org/wiki/Grocery_List)

The language is based on stack operations. So here is an interpretation of the first interation of the code.

**1**
```vichyssoise             
mango                   
vermouth
zucotto
sandwich``` 

Fist item starting with a `v` is skipped and ascii of the first letter of next item is pushed. So 109 is pushed to the stack.

```109  <-TOP/BOTTOM```

Similarly next item starts with a v, so it's ignored and ascii of the following item is taken. Pushed ascii value of `z` to the stack.

```109  <-BOTTOM
122 <-TOP```
The last line here starts with an s which first pop top two values and then subtacts second to top from top.This pushes 13 onto the stack

```13   <-TOP/BOTTOM```

**2**
```lamb
veal
yogurt
vermicelli
zucchini
salmon
fennel seeds
```

Starts a loop. 
Then pushes 1 onto the stack(as shown in previous step)

```13   <-BOTTOM
1   <-TOP```

The last line starts with an `f` and interchanges the top two values of stack.

```1   <-BOTTOM
13   <-TOP```

**3**
```ice cream
carrots
unagi
inca berries
cabbage
upma```

Takes and input and pushes it's ascii to the stack. Let's say first input is `a`.

```1   <-BOTTOM
13
97   <-TOP```

Next, item starts with `c`arrots, so it duplicates value on top.
And then the next item starting with `u` brings the value on top of the stack to BOTTOM

```97   <-BOTTOM
1
13
97   <-TOP```

Similary next item `i`nca berries does the same as above. Let's say the second input is `b`
After the next 3 operations:

```98   <-BOTTOM
97
1
13
97
98   <-TOP```

**4**
```grapes
naan
apples
bananas
almonds
basil```

Next item starting with `g` works like an if statement. Looking here, TOP > second-to-TOP. Hence pushed 1 onto stack.

And then pushes 4. (from `n`)
And then pops top two and adds.

```98   <-BOTTOM
97
1
13
5   <-TOP```

Next item `b`ananas brings value from bottom of stack to top.
And then add top two after popping and then push the result.
And finally brings the other input from bottom of stack

```1   <-BOTTOM
13
103 
97   <-TOP```

**5**
```fenugreek
potatoes
pie
soy beans
eggs
tunafish```

Interchange the op two value of stack (`f`)
Pop and print the top. (`p`)
Pop and print the top again. (`p`)
We see here that our second input is the one that will be changed each time.

```1   <-BOTTOM
13   <-TOP```

```Printed: ga```

Next item `s`oy beans, subtract top two values.
`e` checks for an end for the loop. So here we understand that, the loop is running 13 times. Hence 26 characters.

```12   <-TOP/BOTTOM```

## Solution

```python
a = "4cum77itQdKy4r7c~rm5u05plN"
o = ""
for i in range(0,26,2):
    if((ord(a[i]) - 5) > ord(a[i+1])):
        o = o + a[i+1]
        o = o + chr(ord(a[i]) - 5)
    else:
        o = o + a[i+1]
        o = o + chr(ord(a[i]) - 4)
```
## Flag

shaktictf{c0mp73tedMyGr0c3ry5h0pp1Ng}




