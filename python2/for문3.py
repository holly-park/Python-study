#100 90 80 70 60 ... 10
for i in range(100, 1, -10):
    print("{:3}".format(i),end='')
print()

computer = ["python", "Artificail Intelligence", "Machine Learning", "Deep learning",
              "perceptron", "sigmoid"]

for index in range(0, len(computer)):
    print(computer[index])

for index in range(0, len(computer),2):
    print(computer[index])

a = [1,3,5,7,9]
b = ['일', '삼', '오', '칠', '구']
c = ['가', '다', '마', '사', '자']

for a1, b1, c1 in zip(a,b,c):
    print(a1, b1, c1)

#합계구하기
a = [1,3,5,6,7,2]

#반복구조 s=a[0]+a[1]+a[2]+a[3]
#s1 = a[0], s2 = s + a[1] 
#s=0, s = s + a[n]  처음에 초기값 0이 있어야 함

s=0
for i in range(0,len(a)):
    s= s+a[i]
print("합계: ", s)

#또는
s=0
for i in a:
    s = s + i
print("합계: ", s)