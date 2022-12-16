# Clicky

### Description

You are a Secret Agent appointed to destroy a planet but you don't have resources to do that, but you have access to Death Star's deadly weapon Superlaser. You need to enter the correct pin for the superlaser to launch.

Your companion invaded their system and recovered a file which has the pin hidden in the file. All you have to do is find the correct sequence of numbers to launch the superlaser.


#### Note: Enter the right sequence of numbers separated by an underscore and wrap it around the flag format given.

Flag format : flag{...}

<hr>

### Solution

The given file is an executable, but for basic analysis we use the tool named as DIE to find more details about the file.

![](https://i.imgur.com/rV4iKl4.png)

The analysis indicates that it is dotnet file, thus we use [dnspy](https://github.com/dnSpy/dnSpy) to disassemble the executable.

![](https://i.imgur.com/MWAmaPk.png)


Navigate to the code part of the file via this path and now you could see the c# code for the file.


Here we are asked to find the correct sequence of buttons that needs to be clicked in order to get the win statement.

On observing the code, we could see this pattern

![](https://i.imgur.com/JvDvoIO.png)
![](https://i.imgur.com/G74d8bL.png)

On clicking button 5, there is a check to ensure that the next button, that is, button 7 is clicked, thereafter it checks if button 3 is clicked and consequentively for button 1. If all this buttons are clicked in the given order, we get the final statement. 


Button 5, 7, 3 and 1 are initialized as 429, 529, 216 and 88.

![](https://i.imgur.com/Rzi8TQS.png)

Thus we click buttons 429, 529, 216 and 88 in the given order to get the win statement.

##### Flag : shaktictf{429_529_216_88}
