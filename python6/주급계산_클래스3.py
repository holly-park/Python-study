class WeekPayData:
    name=""
    week_time=0
    per_pay=0
    payment=0
    #생성자 
    def __init__(self, name="", week_time=0, 
              per_pay=0):
        self.name = name 
        self.week_time = week_time 
        self.per_pay = per_pay 

    def process(self):
        self.payment= self.week_time * self.per_pay
    
    def print(self):
        print(self.name, self.per_pay, 
              self.week_time, self.payment)


class WeekPayMgr:
    dataList = list()

    def __init__(self):
        self.dataList.append(
            WeekPayData("허재", 40, 10000))
        self.dataList.append(
            WeekPayData("최동원", 40, 40000))
        self.dataList.append(
            WeekPayData("박정태", 30, 15000))
         
    def output(self):
        for item in self.dataList:
            item.process() 
            item.print() 

    def menuDisplay(self):
        print("1.추가")
        print("2.출력")
        print("3.정렬")
        print("4.불러오기")
        print("5.저장하기")
        print("0.종료")
        
    def start(self):
        while(True):
            self.menuDisplay()
            sel = input("선택 : ")
            if sel=="1":
                self.append() 
            elif sel=="2":
                self.output()
            elif sel=="3":
                self.sort()
            else:
                break

    def append(self):
        data = WeekPayData()#새로운객체만들고 
        data.name=input("이름 : ")
        data.week_time=int(input("근무시간 : "))
        data.per_pay=int(input("시간당금액"))
        
        self.dataList.append(data)

    def sort(self):
        tempList = sorted(self.dataList, 
            key=lambda data:data.name)
        for item in tempList:
            item.process()
            item.print()
    def load(self):
        f=open("주급.txt", "r", encoding="utf-8")
        dataLines=f.readline()
        for item in dataLines:
            data = item.split(",")
            wd = WeekPayData()
            wd.name = data[0]
            wd.week_time=int(data[1])
            wd.per_pay=int(data[2])
            self.dataList.append(wd)
            #data=>WeekPayData 객체 만들어서 dataList객체 추가하기
        f.close()

mgr = WeekPayMgr()
mgr.start()

