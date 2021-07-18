#zh3r0-ctf 2021

##babyre - Reversing

##Description
!(https://github.com/revathi2001/files-required-for-writeups/blob/main/Selection_174.png)
```Its BabyRE, you should be able to solve it without angr. even the stego guys solved this.```

- ![babyre](https://github.com/revathi2001/files-required-for-writeups/blob/main/babyrev)


##Solution
- Opening file in ghidra we can see strings ```CORRECT PASSWORD``` and ```INCORRECT PASSWORD```, going to corresponding function we can see following code.
```
void FUN_00101600(undefined8 param_1,undefined4 param_2,int param_3,undefined8 param_4)

{
  long lVar1;
  undefined8 uVar2;
  
  wattr_on(param_1,0x80000,0);
  lVar1 = FUN_00101560(param_4);
  if (lVar1 == 0) {
    wattr_on(param_1,0x100,0);
    mvwprintw(param_1,param_2,param_3 + 2," CORRECT PASSWORD ");
    uVar2 = 0x100;
  }
  else {
    wattr_on(param_1,0x400,0);
    mvwprintw(param_1,param_2,param_3 + 2,"INCORRECT PASSWORD");
    uVar2 = 0x400;
  }
  wattr_off(param_1,uVar2,0);
  return;
}
```

- In the above code our input is passed to ```FUN_00101560``` and if return value is zero ```CORRECT PASSWORD``` is printed.
```
long FUN_00101560(char *param_1)

{
  int iVar1;
  size_t sVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long in_FS_OFFSET;
  undefined local_58 [16];
  undefined local_48 [16];
  undefined8 local_38;
  long local_30;
  
  local_30 = *(long *)(in_FS_OFFSET + 0x28);
  local_58 = (undefined  [16])0x0;
  local_48 = (undefined  [16])0x0;
  sVar2 = strlen(param_1);
  lVar3 = 1;
  if (sVar2 == 0x20) {
    puVar5 = (undefined8 *)local_58;
    do {
      puVar6 = puVar5 + 1;
      uVar4 = FUN_001014d0(param_1);
      *puVar5 = uVar4;
      param_1 = param_1 + 8;
      puVar5 = puVar6;
    } while (puVar6 != &local_38);
    iVar1 = memcmp(local_58,&DAT_00104020,0x20);
    lVar3 = (long)iVar1;
  }
  if (local_30 == *(long *)(in_FS_OFFSET + 0x28)) {
    return lVar3;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();

}
```
- In the above function our input is splitted into 4 parts and passed to ```FUN_001014d0```.
```
long FUN_001014d0(long param_1)

{
  long *plVar1;
  long *plVar2;
  ulong uVar3;
  long lVar4;
  long in_FS_OFFSET;
  undefined8 local_18;
  long local_10 [2];
  
  lVar4 = 0;
  local_18._0_1_ = 0;
  local_10[0] = *(long *)(in_FS_OFFSET + 0x28);
  local_18 = 0;
  while( true ) {
    plVar1 = &local_18;
    uVar3 = (ulong)*(byte *)(param_1 + lVar4);
    while( true ) {
      plVar2 = (long *)((long)plVar1 + 1);
      *(byte *)plVar1 = (byte)(((uint)uVar3 & 1) << ((byte)lVar4 & 0x1f)) | (byte)local_18;
      if (local_10 == plVar2) break;
      local_18._0_1_ = *(byte *)plVar2;
      plVar1 = plVar2;
      uVar3 = uVar3 >> 1;
    }
    lVar4 = lVar4 + 1;
    if (lVar4 == 8) break;
  }
  if (local_10[0] == *(long *)(in_FS_OFFSET + 0x28)) {
    return local_18;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```
- The above function is converted to python code as follows.
```
x=bytes.fromhex("a4adc0a3fd7fab00e8d5e248dabffd00d140f2c47bbf76008707d5adae82fd00")
flag = [0]*32

for i in range(4):
    x1=x[(i*8):(i*8)+8]
    for k,st in enumerate(x1):
        for j in range(8):
            flag[i*8+j] |= ((st>>j) & 1) << k
        
print("".join([chr(x) for x in flag]))
```

##Flag
```
zh3r0{4_b4byre_w1th0ut_-O3_XDXD}
```
