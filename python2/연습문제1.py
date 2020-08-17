#1
name = input("이름: ")
kor = int(input("국어: "))
eng = int(input("영어: "))
mat = int(input("수학: "))
total = kor +eng + mat
avg=total/3
print("{} {} {}".format(name, total, avg))

#2
print(13%2 == 0)

#string-readonly
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#파이썬은 모든 변수가 참조형태이다
#대상을 직접 저장하지 않고 대상에 대한 주소를 저장한다

a=[1,3,5,4,2]
b=a #데이터가 아니라 참조가 복사된다
a.sort()
a.reverse()
print("가공된 값: ", a)
print("원본: ", b)
print(id(a), id(b))

print( a is b)  #둘이 같은 객체를 참조하느냐
b= a[:] #실제로 대상을 다시 만들어서 복사(hard copy)
print( a is b)

b[0] = 100
print(a,b)

#외부에서 파이썬 모듈을 들고올 수 있다 - import
#패캐지: 라이브러리 묶음
#from 패키지명 import 라이브러리명
#특정패키지로부터 해당 라이브러리만 메모릴 가지고 와라
from copy import copy
a=[1,2,3,4,5]
b=copy(a) #실제로 대상을 다시 만들어서 복사
a[0]=10
print(a,b)
print(a is b)

#['Life', 'is', 'too', 'short'] 조인하라
#JOIN은 문자열 결합함수
s=['Life', 'is', 'too', 'short']
s2=" ".join(s)  #" " 안에 공백이나 컴마(,)를 주면 리스트의 요소들이 공백이나 컴마를 가지고 조인함
print(s2)


#pop
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B')) #dictionary에서 키 값을 제거할 때 
