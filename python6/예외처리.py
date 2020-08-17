try:    #보호블럭(예외가 발생할 수 있는 코드들)
    x=int(input("정수: "))
    print(x*10)
except ValueError:  #예외처리 구문
    print("정수를 입력하셔야 합니다")
except:
    print("원인을 모르는 오류입니다")
   
#try구문 안에서 문제가 발생하면 except구문 뒤로 점프한다
print("둘다 실행됨")
