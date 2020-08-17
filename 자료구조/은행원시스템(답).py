class BankSystem:
    #멤버변수
    queue=[]
    number=0 #고객 대기번호
    def client(self):
        self.number+=1 #고객번호 증가
        self.queue.append(self.number)
        print("손님의 대기 번호는 {}이고 현재 {}명 대기중입니다.".format(self.number, len(self.queue)))
    
    def bank(self):
        if len(self.queue)==0:
            print("대기중인 손님이 없습니다.")
            return
        num=self.queue.pop(0)
        print("{}번 손님 나오세요.".format(num))
        print("총 대기인원은 {}명입니다.".format(len(self.queue)))
    
    def start(self):
         while(True):
            print("선택하세요")
            print("1.손님")
            print("2.은행원")
            print("0.종료")
            sel=input("선택: ")
            if sel=="1":
                self.client()
            elif sel=="2":
                self.bank()
            else:
                return

mgr=BankSystem()
mgr.start()