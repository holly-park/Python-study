"""구구단을 출력하는 함수
    mygugu(3,5)"""

def mygugu(start,end):
   for i in range(start, end+1):
      print("***", i, "단***")
      for j in range(1,10):
          print("%3d x %3d = %3d"%(i,j,i*j))


mygugu(3,5)




def mygugu1(start, end):
    if start>end:
        print("앞에 숫자가 더 작은게 와야 합니다")
        return #함수가 종료된다.(문제가 생기면 끝내고 나오는게 더 나음)
    for i in range(start, end+1):
        print("***", i, "단***")
        for j in range(1,10):
          print("%3d x %3d = %3d"%(i,j,i*j))


mygugu1(2,4)
