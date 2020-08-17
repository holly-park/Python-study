class Stack:
    #변수들은 외부에서 접근 하지 못하게 전부 private권한으로
    __MAX=5   #스택의 최대 크기. 이 변수가 private라서 클래스에서 외부에서 못 고치기 때문에 ___를 함(데이터은닉)
    __buffer=list()   #객체이지, 데이터공간이 아님
    __top=-1 #가장 마지막에 있는 최신데이터의 인덱스를 간직하는 변수. -1의 뜻은 스택의 underflow상황(stack empty)
    def __init__(self):
        for i in range(0,self.__MAX):
            self.__buffer.append("")
    def isFull(self): #스택이 꽉차면 True
        if self.__top==self.__MAX-1:
            return True
        else:
            return False
    def isEmpty(self):  #스택이 empty면 True아니면 False
        if self.__top==-1:
            return True
        else:
            return False
    def push(self, data):    #스택에 데이터 넣기
        if self.isFull():
            print("Stack overflow")
            return
        self.__top += 1
        self.__buffer[self.__top]=data
    def pop(self):     #스택에서 데이터 하나 제거
        if self.isEmpty():
            print("Stack underflow")
            return None
        r = self.__buffer[self.__top]
        self.__top -=1
        return r
    def peek(self):     #스택의 최상위 데이터 확인용 함수
        if self.isEmpty():
            print("Stack underflow")
            return None
        r = self.__buffer[self.__top]
        return r

s=Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
s.push("F")

while(not s.isEmpty()):
     print(s.pop())

