class Parent:
    def functionA(self):
        print("------A------")
    def functionB(self):
        print("------B------")
    def functionC(self):
        print("------C------")
    
    def process(self):
        self.functionA()
        self.functionB()   #functionB만 다시 만들어 써라
        self.functionC()
    
class Child(Parent):
    def functionB(self):    #콜백함수(시스템이 호출)
        print("-----------------")
        print("@@@@@@@@@@@@@@@@@")
        print("-----------------")

    


c = Child()
c.process()

