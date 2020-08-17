#for문 안에 for문이 들어간다

for i in range(1,6):
    for j in range(1,6):
        print("i=", i, "j=", j)

#i가 1일 때 j=1,2,3,4,5
#i가 2일 때 j=1,2,3,4,5
#i가 3일 때 j=1,2,3,4,5
#i가 4일 때 j=1,2,3,4,5
#i가 5일 때 j=1,2,3,4,5 전부 25번 수행된다

#구구단 3단에서 5단까지
for i in range(3,6):
    print("****",i,"단****")
    for j in range(1,10):
        print("%3d x %3d = %3d" %(i,j,i*j))

    print()

for i in range(1,6):
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range(1,6):
    for j in range(1,7-i):
        print("*", end="")
    print()


k=1
for i in range(0,10):
    for j in range(0,10):
        print("{:3}".format(k), end='')
        k+=1
    print()


#A~Z: 65 66 67 68
print(ord('A'))  #ord: 문자들의 코드 반환
print(ord('B'))
print(ord('C'))
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('0'))
print(ord('1'))

"""
문자열 "45" ->52 53    문자저장이 파이썬은 2byte(unicode)
숫자 45 -> 45        
"""

print(chr(100))   #d

base_a=ord('A')
for i in range(0,26):
    print(chr(base_a + i))


for i in range(0,26):
    print(ord('A'))
    