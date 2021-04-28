# Deceev 

## Challenge Writeup

This challenge basically acts as a base64 encoding service where whatever string you give as a binary the base64 encoded string is returned, or at least tahts what it looks like at first sight. Well, the challenge name suggests that it is a deceptive challenge. 
The challenge in its normal behaviour does not enter functions that seem suspicious. 

```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int64 v3; // rdx
  __int64 v4; // rdx
  int result; // eax
  __int64 v6; // [rsp-30h] [rbp-30h]
  __int64 v7; // [rsp-28h] [rbp-28h]
  __int64 v8; // [rsp-20h] [rbp-20h]
  const char *v9; // [rsp-18h] [rbp-18h]

  __asm { endbr64 }
  sub_10E0("Enter the string you want to encode :\t", argv, envp);
  ((void (__fastcall *)(__int64, __int64))sub_10F0)(256LL, _bss_start);
  sub_10E0("%d %d %d %d %d\n", 47LL, 48LL);
  v3 = ((__int64 (__fastcall *)())sub_10D0)();
  v6 = ((__int64 (__fastcall *)(__int64))b64_encode)(v3);
  sub_10E0("encoded: %s\n", v6, v4);
  v7 = b64_decoded_size(v6) + 1;
  v8 = sub_1110(v7);
  if ( (unsigned int)b64_decode(v6, v8, v7) )
  {
    if ( argc == 2 )
    {
      v9 = argv[1];
      sub_1110(256LL);
      ZDNjMTN2Mw(v9);
    }
    *(_BYTE *)(v8 + v7) = 0;
    sub_10B0(v8);
    sub_10C0("Good Day!");
    result = 0;
  }
  else
  {
    sub_10C0("Decode Failure");
    result = 1;
  }
  return result;
}

```
<ins>Checker Code</ins>

```cpp
__int64 __fastcall ZDNjMTN2Mw(__int64 a1)
{
  __int64 v1; // rax
  __int64 v2; // rax
  __int64 v4; // [rsp-10h] [rbp-10h]

  __asm { endbr64 }
  v4 = sub_1110(256LL);
  manipulate(a1, 0LL, v4);
  v1 = sub_10D0(v4);
  v2 = b64_encode(v4, v1);
  if ( !(unsigned int)sub_1100(
                        v2,
                        "c2JodWFna2d0eWktY210M2Y1ezVkYjN1Y2czZ3B5dC0xbTAzbjVfNTFiNXVfZzNndnkzLXJteTN3NWg1M2JydTNnfWc=") )
    sub_10C0("\nYup, you got me :P\nYour input is your flag!!");
  return sub_10C0("Exiting peacefully");
}
```

So taking a deeper look at the decompilation from ghidra/IDA and compare it with another base64 encoding code from online you can notice the differance in the charset used for encoding (This is the intended solution :P).

On going through the path followed by your input you can see that your input is being modified at alternate indices with chars from the string `buggy-m355`. This input goes further for the encoding process. 

Decoding the hardcoded b64(like)`c2JodWFna2d0eWktY210M2Y1ezVkYjN1Y2czZ3B5dC0xbTAzbjVfNTFiNXVfZzNndnkzLXJteTN3NWg1M2JydTNnfWc=` string with the charset used in the binary gives you this string.

`flag = 'sbhuagkgtyi-cmt3f5{5db3ucg3gpyt-1m03n5_51b5u_g3gvy3-rmy3w5h53bru3g}g'[::2]`

### Flag

`shaktictf{d3c3pt10n_15_3v3rywh3r3}`

Which is the flag.
Hope you liked the challenge!!