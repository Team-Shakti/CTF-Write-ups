# Fusk



### Challenge Concept

Vey simple basic RE challenge where the binary decompilation itself can give you the required arrays to reverse the xor algo used to encrypted with a recursive fib sequence function. 

```cpp
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  unsigned int v3; // eax
  __int64 result; // rax
  int v5; // [rsp-D0h] [rbp-D0h]
  int i; // [rsp-CCh] [rbp-CCh]
  __int64 v7; // [rsp-C8h] [rbp-C8h]
  __int64 v8; // [rsp-48h] [rbp-48h]
  unsigned __int64 v9; // [rsp-20h] [rbp-20h]
  __int64 v10; // [rsp-8h] [rbp-8h]

  __asm { endbr64 }
  v9 = __readfsqword(0x28u);
  v5 = 3;
  sub_10B0(&v8, 32LL, stdin);
  for ( i = 0; i < sub_1090(&v8); ++i )
  {
    v3 = v5++;
    *(&v10 + i - 48) = sub_11A9(v3) ^ *(&v10 + i - 64);
  }
  if ( sub_11E9(&v7) )
    sub_1080("You Win");
  else
    sub_1080("Try Again..!");
  result = 0LL;
  if ( __readfsqword(0x28u) != v9 )
    result = sub_10A0();
  return result;
```
The recursive function being, function: `sub_11E9(&v7)`

### Flag

flag = shaktictf{s1mpl3_movfu5ca7i0n}
