class Person:  #클래스의 정의
    name="홍길동"
    age=18
    def print(self):
        print(self.name, self.age) 
        #self에는 p1의 주소(객체의 주소)가 저장됨
        #이를 통해 인스턴스 객체의 이름공간에 접근

#객체 만듦
p1 = Person()   #클래스의 이름으로 객체 또는 인스턴스를 만듦

print(p1.name, p1.age)

#멤버들을 클래스명으로 접근 가능하다
print(Person.name, Person.age)
Person.phone = "010-0000-0000"  #이 방법이 되기는 하지만 이렇게 코딩하지 말 것
print(p1.phone)