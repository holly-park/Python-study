"""

이름    근무시간  시간당급여액  주급
-----------------------------------
홍길동    15        10000     150000
장길산    40        10000     400000
임꺽정    30        12000     360000
-----------------------------------
총 지불액                     850000

"""

#리스트만 사용하는 방법
"""
1.4개의 리스트 필요
2.리스트 안에 요소 입력받기
"""
nameList=[]  #[]와 list() 똑같음
workList=[]
perpayList=[]
payList=[]

for i in range(1,4):
    name=input("이름: ")
    work_time=int(input("근무시간: "))
    perpay=int(input("시간당급여액: "))
    nameList.append(name)
    workList.append(work_time)
    perpayList.append(perpay)

for i in range(0, len(nameList)):
    pay=workList[i]*perpayList[i]
    payList.append(pay)

totalpay=0
for i in range(0,len(payList)):
    totalpay=totalpay+payList[i]

print("이름\t근무시간\t시간급여\t주급")
print("-"*50)
for i in range(0,len(nameList)):
    print(nameList[i], end='\t')
    print(workList[i], end='\t')
    print(perpayList[i], end='\t')
    print(payList[i])
print("-"*50)
print("총지급액: ", totalpay)



#딕셔너리를 사용하는 방법
dataList = []
count = int(input("몇명?: "))
for i in range(0, count):
    data = dict()
    data['name']=input("이름: ")
    data['work_time']=int(input("근무시간: "))
    data['per_pay']=int(input("시간당급여액: "))
    dataList.append(data)

for data in dataList:
    data['pay'] = data['work_time']*data['per_pay']
for data in dataList:
    print(data)