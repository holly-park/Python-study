#함수를 정의(만들었다)
def myfunc1():
    print('='*50) #이 함수 하나만 고치면 전체 영향

#함수를 호출한다
myfunc1()
print("   정보1   ")
myfunc1()
print("   정보2   ")
myfunc1()
print("                     정보3")
myfunc1()

def func2(mark,cnt): #매개변수
    print(mark*cnt)

func2("*",20)
func2("!",30)
func2("-",40)
func2("~",35)


#1~n까지 합계를 구하는 함수
def mysum(n):
    """함수 안에서 만드는 변수는 모두 지역변수(함수내에서만 존재한다)"""
    s=0
    for i in range(1, n+1):
        s += i
    return s #값 반환하기

print(mysum(100)) #100은 인수(argument)
#값이 필요한 함수이기 때문에 print(mysum())처럼 값없이 호출될 수 없다
