"""
1.가위
2.바위
3.보

1)컴퓨터가 먼저 생각을 한다. 랜덤한 값을 하나 추출해서 갖고 있다
2)사람에게 1,2,3중 하나 입력
    만약 1이면, 컴퓨터: 바위 사람:가위 ->컴퓨터 승
"""
import random

class computer:
    
    def __init__(self, scissor=0, rock=1, paper=2):
        self.scissor=scissor
        self.rock=rock
        self.paper.paper

    def random(self):
        for i in range(1,2):
            self.a=random.randint(0,2)
            if self.a==0:
                self.a=scissor
            elif self.a==1:
                self.a=rock
            else:
                self.a=paper

class game(computer):
    dataList=[]
    def __init__(self, scissor=0, rock=1, paper=2):
        self.scissor=scissor
        self.rock=rock
        self.paper=paper

    def game(self):
        print("숫자를 입력하세요")
        print("1.가위")
        print("2.바위")
        print("3.보")
        myTurn=input("가위바위보>> ")
        computer.random()
        computer.__init___(self, a)
        print(a)  #부모 클래스 객체의 a
        
    def menuDisplay(self):
        print("1.가위바위보 하기")
        print("2.프로그램 종료")

    def start(self):
        while(True):
            self.menuDisplay()
            sel=input("선택: ")
            if sel=="1":
                self.game()
            else:
                break

