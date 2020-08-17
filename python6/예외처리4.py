def divide(x,y):
    return x/y

try:
    print( divide(5,6))
    #print(divide("5","0"))
    print(divide(5,0))
except Exception as e:
    print(e.arg[0])
finally:
    print("종료합니다")