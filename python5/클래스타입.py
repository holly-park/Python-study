class Person:
    pass
class Bird:
    pass
class Student(Person):  #Person클래스 상속
    pass

p, s = Person(), Student()  #p에는 Person, s에는 student 할당
print(isinstance(p, Person))  #True
print(isinstance(s, Person))  #True
print(isinstance(s, Student)) #True
print(isinstance(p, Student)) #False
#Student 클래스는 Person 클래시의 자식이다
#Student 클래스는 Person의 일종이다
#Person  클래스는 Student의 일종이다
   
print(isinstance(p, Bird))     #False  
print(isinstance(p, object)  ) #True
print(isinstance(int, object)) #True

"""
파이썬의 모든 클래스는 object클래스를 상속받는다
모든 타입이 object를 상속받는다

list 타입 - 파이썬
a = [Person(), Person(), Person()]
b = [Bird(), Bird(), Bird()]
c  = [Student(), Student(), Student()]
d = [object(), object(), object()]

a=Person()   나한테 하나 연결되어있다
b=a          두개째 연결되었다
b=Student()  하나가 마이너스 됐다
a=Bird()     a=Person()은 건들이지 않으며 시스템이 언젠가 삭제

"""
