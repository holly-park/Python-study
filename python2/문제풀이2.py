"""
문제1.정수를 10개 입력받아서 합과 평균을 구하여 출력하기
문제2.정수를 10개 입력받아서 각각 짝수와 홀수의 개수와 평균 구하기
"""

#문제1

myList=[]
s=0
for i in range(0, 10):
  num=int(input("정수를 입력하세요: "))
  myList.append(num)
  s=s+myList[i]
  avg=s/10
  

print("합계: ", s)
print("평균: ", avg)


#문제2 
even_cnt=0
even_sum=0
odd_cnt=0
odd_sum=0
for i in myList:
  if i%2==0:
    even_cnt = even_cnt + 1
    even_sum = even_sum + i
  else: 
    odd_cnt = odd_cnt + 1
    odd_sum = odd_sum + i
print("짝수 개수 {} 짝수평균 {}".format(even_cnt,even_sum/even_cnt))
print("홀수 개수 {} 홀수평균 {}".format(odd_cnt,odd_sum/odd_cnt))