class Person:
    def __init__(self, name="홍길동", phoneNumber="010-0000-0000"):
        self.name=name
        self.phoneNumber=phoneNumber
        print("Person 생성자")
    
    def printInfo(self):
        print("---Person printInfo---")
        print(self.name, self.phoneNumber)

    def callPrint(self):
        self.printInfo()    

    def getName(self):
        return self.name
    def getPhoneNumber(self):
        return self.phoneNumber
    

class Student(Person):
    def __init__(self, name="학생", phoneNumber="010-1111-1111", subject="컴퓨터학과", StudentID="111111"):
        print("Student 생성자")
        #self.name=name
        #self.phoneNumber=phoneNumber
        #부모생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.subject=subject
        self.StudentID=StudentID
        

   #부모method인 printInfo 메서드를 재정의 한다
    def printInfo(self):
        print("--------------------")
        print(self.name)
        print(self.phoneNumber)
        print(self.subject)
        print(self.StudentID)
        print("--------------------")



p,s = Person(), Student()
#p입장에서 내가 가지고 잇는 printInfo가 아니고
#각자 자기 객체것 호출함
p.printInfo() #Person 클래스의 printInfo 함수 호출
#-----printinfo호출하기
s.printInfo() #Student 클래스의 printInfo 함수 호출


s2=Student()
print(s2.getName())
print(s2.getPhoneNumber())

p.callPrint() #Person 클래스의 printInfo 함수 호출
s.callPrint() #Student 클래스의 printInfo 함수 호출

