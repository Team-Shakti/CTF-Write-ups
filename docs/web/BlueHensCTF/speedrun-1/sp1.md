# speedrun-1

## Description
![a](https://user-images.githubusercontent.com/47029515/112105169-182e1b80-8bd2-11eb-81ee-628ee0169b08.png)
  
## Solution
When we visit the url we find this static page that just says hello User 2

![1a](https://user-images.githubusercontent.com/47029515/112104958-d309e980-8bd1-11eb-8f60-ed01b75c9822.png)

We notice there is a session cookie. PHPSESSID is generally produced using MD5.

![2a](https://user-images.githubusercontent.com/47029515/112104964-d56c4380-8bd1-11eb-92fb-3a9900b40177.png)

`c81e728d9d4c2f636f067f89cc14862c` is the MD5 hash of `2`. Let's try changing the value. `MD5(1) = c4ca4238a0b923820dcc509a6f75849b`

![3a](https://user-images.githubusercontent.com/47029515/112104971-d7ce9d80-8bd1-11eb-8507-c4bf2a7b9d14.png)

This gave us the flag:

![4a](https://user-images.githubusercontent.com/47029515/112104979-da30f780-8bd1-11eb-8794-354e5ca48716.png)
