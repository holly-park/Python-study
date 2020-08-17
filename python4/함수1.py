#함수 주소 확인하기
def times(a,b):
    return a*b

print(times)  #괄호 없음 - 함수 호출한 것이 아님
print(times(4,5))  #함수호출

def times2(a,b):
    a=a*2
    b=b*2
    return a,b  #파이썬 동시에 반환된 값을 튜플로 만들어 준다

a=10
b=10
a,b = times2(a,b)
print(a,b)

a=times2
print(a(7,9))  #변수 a에 함수를 저장할 수 있다

print(globals())  #생성된 함수 객체들을 볼 수 있다

print(dir(__builtins__))  #내장 영역의 이름이 저장되어 있는 리스트

print(sum([1,3,5,7,9]))

def display():
    print("값 반환을 하지 않는 함수입니다") #리턴이 없으면 값반환 할 수 없음

print(display())  
#함수가 값을 반환하지 않으면 None객체를 반환한다