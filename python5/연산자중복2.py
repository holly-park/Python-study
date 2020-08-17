class Person:
    def __init__(self, name="홍길동", age=24):
        self.name=name
        self.age=age

    def print(self):
        print(self.name, self.age)

    #==비교연산자: 서로 같은 객체를 참조하고 있는가?
    #만약 내용을 공유하고 싶다면
    def __eq__(self, other):
        if self.name == other.name and self.age==other.age:
            return True
        else:
            return False
    def __str__(self):
        return "{} {}".format(self.name, self.age)


p1 = Person()
p2 = Person()
if p1 == p2:
    print("둘이 같다")   #__ep__를 만들었을 때
else:
    print("둘이 다르다")  ##__ep__를 만들지 않았을 때

print(p1)  #__str__을 쓰면 p1을 호출한다