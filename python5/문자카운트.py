"""
I like star
a - 1
b - 0
c -

...
i - 1
count=[0,0,0,0,0,0,0,0,.....] 26개
'a'a -> count[0]
ord('c') - ord('a') ->2
"""

s=input("아무키나 누르세요: ")
count=[]
for i in range(0,26):
    count.append(0)

for c in s:
    if ord(c)>=ord('a') and ord(c)<=ord('z'):
        count[ord(c)-ord('a')]+=1
    if ord(c)>=ord('A') and ord(c)<=ord('Z'):
        count[ord(c)-ord('A')]+=1

for i in range(0,26):
    print(chr(ord('A')+i), "==>", count[i])
