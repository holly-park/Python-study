def changeValue(xList):
    for i in range(0, len(xList)):
        xList[i]=xList[i]*2
    """
    for x in xlist: 
        x=x*2 이때 x는 xList의 값 하나만 읽어와서 사용할 뿐 본래의 xList 와는 상관없다
    """

a=[1,2,3,4,5]
changeValue(a)
print(a)

def myfunc1(a=10, b=20, c=30):
    return a+b+c

print(myfunc1())       #60
print(myfunc1(1))      #51(1+20+30)
print(myfunc1(1,2))    #33(1+2+30)
print(myfunc1(1,2,3))  #6(1+2+3)

def myfunc2(x, a=10, b=20, c=30): #기본 인자값이 없는 인자를 먼저 써야 함
    return x+a+b+c

print(myfunc2(10))     #70(10,10,20,30)
z=myfunc2(10,b=2)
print(z)   #52(10,10,2,30)

#가변 인자 리스트(*를 붙인다)
def myfunc3(*arg):   #각 요소들의 합계 구해서 반환하기
    s=0
    for item in arg:
        s = s + item
    return s

print(myfunc3(1))   #1
print(myfunc3(10,20,30,40,50))   #150

#정의되지 않은 인자 처리(**를 붙인다)
def myfunc4(**info):
    print(info['userid'])
    print(info['password'])
    print(info['username'])

myfunc4(userid='user01', password='1234', username='홍길동')