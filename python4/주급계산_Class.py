class WeekPay:
    name="마이워터"
    work_time = 40
    per_day = 10000
    def process(self):
        self.pay = self.work_time*self.per_day
    def output(self):
        print(self.name, self.work_time, self.per_pay, self.pay)
    def input(self):
        self.name=input("이름: ")
        self.work_time=int(input("근무시간: "))
        self.per_pay=int(input("시간당급여액: "))


wp = WeekPay()
wp.input()
wp.process()
wp.output()

