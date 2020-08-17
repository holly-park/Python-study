#배열의 범위를 벗어나는 에러
a=[1,2,3,4,5]

try:
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    print(a[5])
except IndexError as e:
    print(e.args[0])
except:
    print("알 수 없는 에러입니다")
else:
    print(sum(a))
finally:
    print("이 구문은 무조건 실행된다")
    #에러의 발생 유무와 관계없이 마무리작업이 필요할때 finally


