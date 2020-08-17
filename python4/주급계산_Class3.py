class WeekPayData:
    name=""
    weektime=0
    perpay=0
    payment=0
    def __init__(self, name="", weektime=0, perpay=0):
        self.name=name
        self.weektime=weektime
        self.perpay=perpay
    def process(self):
        self.payment=self.weektime*self.perpay
    def output1(self):
        print(self.name, self.perpay, self.weektime, self.payment)

class WeekPayMgr:
    dataList=[]
    def __init__(self):
        self.dataList.append(WeekPayData("마이워터",40,10000))
        self.dataList.append(WeekPayData("마이컴",30,40000))
        self.dataList.append(WeekPayData("마이팬",20,10000))
    def append(self):
        data=WeekPayData() #새로운 객체를 만들기
        data.name=input("이름: ")
        data.weektime=int(input("근무시간: "))
        data.perpay=int(input("시간당급여액: "))
        self.dataList.append(data)
    def output2(self):
        for item in self.dataList:
            item.process()
            item.output1()
    def menuDisplay(self):
        print("1.추가")
        print("2.출력")
    def start(self):
        while(True):
            self.menuDisplay()
            sel=input("선택: ")
            if sel=="1":
                self.append()
            elif sel=="2":
                self.output2()
            else:
                break

mgr = WeekPayMgr()
mgr.start()