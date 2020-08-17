class BankMgr:
    def __init__(self, waitNum=1, waitPer=0, Bnum=1, Bper=0):
        self.waitNum=waitNum  #손님:대기번호
        self.waitPer=waitPer  #손님:대기인수 - 은행 절차에 따라서 0부터 다시 카운트
        self.Bnum=Bnum        #은행:번호표(queue) - 번호가 끝나고 '은행'을 누르면 대기중인 손님이 없다고 나옴
        self.Bper=Bper        #은행:대기인수(stack) -이 대기인수가 0이 되면 손님의 대기인수도 0이 됨
     
    def menuDisplay(self):
        print("선택하세요")
        print("1.손님")
        print("2.은행원")
        print("0.종료")
        
    def start(self):
        self.count=0
        self.count2=0
        while(True):
            self.menuDisplay()
            sel=input("선택: ")
            if sel=="1":
                self.count += 1
                self.customer()
            elif sel=="2":
                self.count2 += 2
                self.banker()
            else:
                break
    
    def customer(self):
        self.waitNum=self.count  #sel에 1을 입력할 때마다 대기번호가 1씩 늘어남
        self.waitPer=self.count  #sel에 1을 입력할 때마다 대기인수가 1씩 늘어남
        print("손님의 대기 번호는 {}이고 현재 {}명 대기중입니다.".format(self.waitNum, self.waitPer))
    
    def banker(self):
        self.Bnum=self.waitNum
        self.queue=[]
        self.s=0
        self.queue=list(range(0,self.Bnum+1))
        while len(self.queue)!=0:
            self.Bnum=self.queue.pop(0)
            return self.s
        print(self.s)
    #     self.output()

    # def output(self):
    #     self.Bper=self.waitPer
    #     if self.Bnum == self.queue[0]:
    #         print("대기중인 손님이 없습니다.")
    #     else:
    #         self.stack=list(range(0,self.Bper+1))
    #         self.Bper=self.stack.pop()
    #         return self.Bper
    #         print("{}번 손님 나오세요. 총 대기인원은 {}명입니다.".format(self.Bnum, self.Bper))
    #     self.waitPer=self.Bper
        
mgr=BankMgr()
mgr.start()