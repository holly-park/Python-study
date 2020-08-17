

def add(*num):  #입력된 숫자의 합을 구하는 함수
    s = 0
    for i in num:
        s = s+i
    return s


def evenAdd(*num):   #짝수의 합을 반환하는 함수
    s = 0
    for i in num:
        if i%2 ==0:
            s = s+i
        return s

def isEven(num):
    if num%2==0:
        return True
    else:
        return False
    



#def isEvent(*num3):   #짝수면 True, 홀수면 Flase
 #   if num3 %2==0:
        
  #  else:
   #     return False
    



if __name__ == "__main__":
    print(add(1,2,3,4,5))
    print(evenAdd(1,3,5,2,4,6))
    print(isEven(5))
    






