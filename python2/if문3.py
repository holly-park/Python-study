"""
90이상: 수
90미만 80이상:우
80미만 70이상: 미
70미만 60이상: 양
60미만: 가
"""

score=int(input("점수: "))
if score>=90:
    print("수")
elif score>=80:
    print("우")
elif score>=70:
    print("미")
elif score>=60:
    print("양")
else:
    print("가")


"""
문제1. 주급계산
이름, 근무시간, 시간당급여액, 주급을 계산하는데 만약 근무시간이 40시간이 넘는다면 초과부분에 대해서는
시간당급여액의 50%를 특별수당으로 계산하라
그리고 총 금액이 20만원 미만이면 3.3%로 세금을 계산하고
20만원 이상 40만원 미만이면 4.4%
40만원 이상이면 5.5%로 계산하라
print("홍길동님이 근무한 시간은 ()시간이고 시급은 ()이고 주수령액은()이고 수당은()이고
세금은()으로 실수령액은 () 입니다")
"""

"""
1.입력작업 - 계산결과를 가져오는데 필요한 입력데이터가 뭔가 (이름, 시간당급여액, 근무시간)
2.계산
   총액: 근무시간*시간당급여액
   수당: 근무시간이 40 넘어가 때 초과분(근무시간-40)*시간당급여액*0.5
   세금: 20이하 0.033 40이하 0.044 그밖애 0.055
3.출력결과
"""

name=input("이름: ")
work_time=int(input("금주근무시간: "))
per_pay=int(input("시간당급여액: "))

pay=work_time*per_pay
over_pay=0

if(work_time>40):
    over_pay=(work_time-40)*per_pay*0.5
total_pay=pay+over_pay

if total_pay <= 200000:
    tax=total_pay*0.033
elif total_pay <= 400000:
    tax=total_pay*0.044
else:
    tax=total_pay*0.055

real_pay=total_pay-tax
result="{} {} {} {} {} {} {} {}".format(name, work_time, per_pay, pay, over_pay, total_pay, tax, real_pay)

print(result)

#나는 애초에 수당+기본급을 주당급여로 한꺼번에 계산하다보니까 1.5를 곱했고, 그러다니보니까
#수당을 안 받는 경우에 어떠케 표현할지 몰라서 문제 발생함
