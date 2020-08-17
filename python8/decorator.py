def mydecorator(callfunc):
    def func(a,b):
        print("======중간에서 함수 가로채기=======")
        callfunc(a,b)
        print("=================================")
    return func  #마지막에 함수를 반환해야 함


@mydecorator
def myfunc(a,b):
    print(a,b)
    print("데코레이터에 파라미터는 줄 수 없을까?")

myfunc(4,5)