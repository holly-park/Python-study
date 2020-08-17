"""
전역변수 - 함수들이 같이 쓸 수 있는 공유변수
지역변수 - 함수내부에 선언되는 모든 변수들(함수 사용이 종료되면 사라진다)
"""

x=10
def myfunc1():
    #UnboundLocalError: local variable 'x' referenced before assignment
    x=0 #함수 내에서 선언된 x와 함수 밖에서 선언된 x는 다르다
    x=x+5
    return x

print(id(x))
print("함수 호출 후:")
print(myfunc1())



x=10
def myfunc2():
    global x   #밖에 있는 변수를 같이 사용할 것이다(이 기능을 많이 써서 좋을 거 없다)
    print(id(x))
    x=x+5
    return x

print(myfunc2())