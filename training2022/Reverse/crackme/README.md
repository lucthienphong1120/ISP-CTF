# crackme



# Challenge
[Crackme.exe](Crackme.exe)


# Writeup

assume flag = `ABC`, key = `0x50` then:
```
            A           B           C
_______________________________________________            
i = 0       0x50^A      A^B         B^C
key =       A           B           C
_______________________________________________
i = 1       C^A0        A0^B0       B0^C0
key =       A0          B0          C0
_______________________________________________
...
_______________________________________________
i = 2605    C2603^A2604 A2604^B2604 B2604^C2604
key         A604        B2604       C2604
_______________________________________________
i = 2606    C2604^A2605 A2605^B2605 B2605^C2605
key =       A2605       B2605       C2605 
```
Note: *Ax means A value at x round*  
Given row `2606` (in hex) and `key = C2605`
```
B2605 = C2606 ^ key = C2606 ^ C2605 
A2605 = B2605 ^ B2606  
C2604 = A2606 ^ A2605
....
```

As `key` always in range [0..255] (`key` type is `BYTE`):  
code: [crackme.py](crackme.py)

  

# Flag
Flag: `ISPCTF{pl4y1ng_w1th_x0r5}`  
Key: `b`
