"""
1
3
4
5
6
7
9
11
12

라는 내용이 있는 텍스트파일을 불러와서 더하기
"""

f=open("filetest.txt","r")
txList=f.readlines()
f.close()

s=0
cnt=0
for item in txList:
    number=int(item)
    s=s+number
    cnt=cnt+1
  
print(s, s/cnt)  