"""
break: while, for문 등을 중간에 빠져나가고자 할 때 사용된다
       break문은 자신과 가장 가까운 루프를 종료한다
"""

for i in range(1,11):
    if i>=5:
        break
    print(i) #5가되는 순간에 종료되기 때문에 4까지 출력됨

#break문을 많이 쓸 수록 디버깅에 안좋기 때문에 안 쓰게끔 코딩하는게 좋음

for i in range(1,11):
    if i=5:
        continue #5일때 건너뛰고 1,2,3,4,6,7,8,9,10이 찍힌다
    print(i)