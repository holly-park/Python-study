class WeekPay:
    name="마이워터"  #__init__을 선언하면 꼭 이 변수들을 선언안해도 됨
    weektime=40
    perpay=10000
    def setValue(self, name, weektime, perpay):
        self.name=name
        self.weektime=weektime
        self.perpay=perpay

        #생성자-객체가 생성될 때 자동으로 호출됨
        #시스템이 호출자라 이름이 정해져 있다
        #__init__(self)로 정해져 있음
        #한개만(오버로딩x)
    def __init__(self, name="", weektime="", perpay=""):
        self.name=name
        self.weektime=weektime
        self.perpay=perpay
    def output(self):
        print(self.name, self.weektime, self.perpay)

#work1=WeekPay()  생성자를 만들었으니 필요없음
#work1.setValue("화이트하임", 30, 10000)
work1= WeekPay("화이트화임", 50, 2000)
work1.output()
wList = [WeekPay("a", 40, 10000),
         WeekPay("b", 20, 30000),
         WeekPay("c", 50, 15000)]

for work in wList:
    work.output()