g = lambda x,y : x*y
print(g(2,3))

print((lambda x,y: x*y)(3,4))

#map
def sqrt(x):
    x=x*x
    return x

a=map(sqrt, [1,2,3,4,5,6,7,8,9,10])
print(a)   #map자체로는 출력안됨
#for문을 쓰거나 lsit 로 형전환 해야함

for item in map(sqrt, [1,2,3,4,5,6,7,8,9,10]):
    print(item)

for item in map(lambda x:x*x, [1,2,3,4,5,6,7,8,9,10]):
    print(item)

a=list(map(lambda x:x*x, [1,2,3,4,5,6,7,8,9,10]))
print(a)

"""
파이썬의 정렬함수
1.list - 자기순서가 바뀜
2.내장함수 sored - 정렬된 데이터를 반환
"""

a=[5,4,7,8,1,3,10,9,2,6]
b=a[:] #하드카피(새로운 객체 만들고 a값 복사)
a.sort()
print(a)
print(b)
c=sorted(b)
print("original : ", b)
print("sorted : ", c)

mya=[5,4,-7,8,1,-3,10,9,-2,6]
b=mya[:]
a.sort(key=sqrt) #음수값에 관련없이 정렬하고 싶을 때
print(a)
print(b)
c=sorted(b, key=sqrt)
c=sorted(b, key=lambda item:item*item)  #item이라는 이름을 줌
print("original : ", b)
print("sorted : ", c)


students=[
    {"name":"강만수", "kor":90, "eng":80},
    {"name":"김정하", "kor":80, "eng":60},
    {"name":"이민호", "kor":70, "eng":70},
    {"name":"김성훈", "kor":99, "eng":90},
    {"name":"강기정", "kor":95, "eng":70}
]


a=sorted(students, key=lambda item:item['name'], reverse=True) #reverse=True 내림차순 정렬
print(a)

a=["pen","water","desktop","snack","book"]
#filter(조건식, 리스트) 리스트에서 조건을 만족하는 요소만 추출한다
for item in filter(lambda x:len(x) >=5, a):
    print(item)