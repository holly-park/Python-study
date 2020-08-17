import datetime

def work():
    print("현재시간", datetime.datetime.now())
    for i in range(1,10000):
        pass
    print("종료시간", datetime.datetime.now())

def work2():
    print("현재시간", datetime.datetime.now())
    for i in range(1,10000):
        pass
    print("종료시간", datetime.datetime.now())

work()
work2()


#데코레이터로 사용되는 함수는 매개변수가 함수이어야 한다(콜백)
def now_time(callfunc):
    #함수 안에 내부 함수를 만든다. 그리고 반드시 함수 이름을 반환해야 한다
    def inner_func():
        print("현재시간", datetime.datetime.now())
        callfunc() #매개변수로 받아온 함수를 호출한다
        print("종료시간", datetime.datetime.now())
    return inner_func  #now_time이 내부함수를 외부로 반환한다

@now_time
def work3():
    for i in range(1,5000000):
        pass
    print(i)

work3()