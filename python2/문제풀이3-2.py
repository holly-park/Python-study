dataList = [
    {"name":"홍길동", "phone":"010-1234-5678"},
    {"name":"김길동", "phone":"010-1234-5678"},
    {"name":"박길동", "phone":"010-1234-5678"}
]

#list 타입에 요소로 dict타입이
for data in dataList:
    print(data['name'], data['phone'])

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