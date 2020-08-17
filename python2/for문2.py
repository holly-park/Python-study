score=[50,20,55,60,44,50, 70, 65,50,35,90, 100]
result=[] #list타입 객체 만들기
for item in score:
    if item>=60:
        result.append("합격")
    else:
        result.append("불합격")
print(score, result)

for item in zip(score, result): #zip은 여러개의 리스트를 합쳐서 하나의 튜플로 만듦
    print(item)

for item1, item2 in zip(score, result):
    print(item1, "====>", item2)

a=[1,2,3,4,5,6,7,8,9,10]
for item in a:
    print(item)

#숫자리스트 생성해주는 함수 range ->generator ->list로 강제 형전환
a=list(range(1, 10, 2)) #시작값, 종료값, 증감치
print(a)

b=list(range(2, 10, 2))
print(b)

#list, tuple, dict
#generator(일종의 데이터를 계속 생성하는 함수)

#줄바꿈 안하려면
for i in range(1, 101):
   
    print("{:3}".format(i), end=' ')
    if i%10==0: #10개씩 줄바꿈
        print()
print() #마지막에 for문 다 종료하고 줄바꿈하기
