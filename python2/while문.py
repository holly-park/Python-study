"""
while 조건식: 조건식의 결과는 true 또는 false 이다
  문장1   조건식이 True일때만 작동
  문장2   
"""

i=1
while i<=5:
   print(i)
   i=i+1


"""
숫자를 입력받는데 양수가 입력되는 동안 합을 구하고
음수를 들어오면 종료, 0은 안들어온다
"""

s=0
num = int(input("정수: "))
while num>0:
    s= s+num
    num=int(input("정수: "))

print("합계", s)