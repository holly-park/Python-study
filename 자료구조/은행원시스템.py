class BankingSys:
    def __init__(self, waitNum=0, waitPer=0):
        self.waitNum=waitNum
        self.waitPer=waitPer
    
    

class BankMgr:
    def __init__(self, waitNum=0, waitPer=0):
        self.waitNum=waitNum
        self.waitPer=waitPer
 
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
                self.banker()
            else:
                break

    def customer(self):
        self.waitNum=self.count  #sel에 1을 입력할 때마다 대기번호가 1씩 늘어남
        self.waitPer=self.count  #sel에 1을 입력할 때마다 대기인수가 1씩 늘어남

        print("손님의 대기 번호는 {}이고 현재 {}명 대기중입니다.".format(self.waitNum, self.waitPer))
    def queue(self):
        self.queue=[]
        self.result=0
        cnt=0
        for i in range(0, self.waitNum+1):
             cnt +=i
             self.queue.append(cnt)
        while len(self.queue)!=0:
              self.result=self.result+self.queue.pop(0)
              return self.result
    def stack(self):
        self.stack=[]
        self.result2=0
        cnt2=0
        for i in range(0, self.waitPer+1):
            cnt2 +=i
            self.stack.append(cnt2)
        while len(self.stack)!=0:
            self.result2=self.result2+self.stack.pop()
            return self.result2
    
     
    def banker(self):
        queue()
        stack()
        waitPer=result2
        print("{}번 손님 나오세요. 총 대기인원은 {}명입니다.".format(self.result, self.result2))

    # def queue(self):
    #     self.queue=[]
    #     self.result=0
    #     cnt=0
    #     for i in range(0, self.waitNum+1):
    #          cnt +=i
    #          self.queue.append(cnt)
    #     while len(self.queue)!=0:
    #           self.result=self.result+self.queue.pop(0)
    #           return self.result
    # def stack(self):
    #     self.stack=[]
    #     self.result2=0
    #     cnt2=0
    #     for i in range(0, self.waitPer+1):
    #         cnt2 +=i
    #         self.stack.append(cnt2)
    #     while len(self.stack)!=0:
    #         self.result2=self.result2+self.stack.pop()
    #         return self.result2
        
       
        
        
        
        

mgr=BankMgr()
mgr.start()

        
   
