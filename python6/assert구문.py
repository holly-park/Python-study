def add(a,b):
    if type(a)!=int or type(b)!=int:
        raise TypeError("정수만 입력하세요")
    return a+b
def sub(a,b):
    assert type(a) == int and type(b)==int, "정수만 넣으세요"
    return a-b
def mul(a,b):
    if type(a)!=int or type(b)!=int:
        raise TypeError("정수만 입력하세요")
    return a*b
def div(a,b):
    if type(a)!=int or type(b)!=int:
        raise TypeError("정수만 입력하세요")
    if b==0:
        raise ZeroDivisionError("0으로 나누려는 시도가 있습니다.")
    return a/b
try:
    print(add(4,3))
    print(sub(4,"3"))
    print(mul(4,3))
    print(div(4,0))  
    #div만 두번째 인자에 0이 들어가면 안되는데, 그냥 모든걸 0들어가면 안된다고 하고, div를 제외한
    #나머지 부분을 raise처리한다
except TypeError:
        print("Type Error")
except ZeroDivisionError as e2:
        print(e2.args[0])