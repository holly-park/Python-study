"""
문제1. 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
...
ZABCDEFGHIJKLMNOPQRSTUVWXY

문제2.
    *
   ***
  *****
 *******
*********
"""


#문제1
for i in range(0,26):
    k=ord('A')+i
    for j in range(0,26):
        print( chr(k), end="")
        k=k+1
        if k>ord('Z'):
            k=ord('A')
    print()


#문제2
"""
행 i 5개: 0,1,2,3,4
공백개수 4        별 1
        3           3
        2           5
        1           7
        0           9
공백개수 +i =4    2*i-1
         =4-i
"""
for i in range(0,6):
    for j in range(0, 5-i):
        print(' ', end='')
    for j in range(0, 2*i-1):
        print('*', end='')
    print()

