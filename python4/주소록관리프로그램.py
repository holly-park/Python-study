#이름, 전화번호, 이메일

class AddressList:
    name=""
    contact=""
    email=""
    def __init__(self, name="", contact="", email=""):
        self.name=name
        self.contact=contact
        self.email=email
    def output1(self):
        print(self.name, self.contact, self.email)

class ListMgr:
    adrList=[]
    def __init__(self):
        self.adrList.append(AddressList("홍길동", "28533-22", "djdk@cris.com"))
        self.adrList.append(AddressList("김길동", "33533-22", "22gdk@cris.com"))
        self.adrList.append(AddressList("이길동", "68533-22", "sdkk@cris.com"))
    def append(self):
        data=AddressList()
        data.name=input("이름: ")
        data.contact=input("전화번호: ")
        data.email=input("이메일: ")
        self.adrList.append(data)
    def output2(self):
        for item in self.adrList:
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

mgr=ListMgr()
mgr.start()
