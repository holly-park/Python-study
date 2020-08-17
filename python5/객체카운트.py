class CountManager:
    __insCount=0  #__을 붙이면 접근권한이 private로 바뀐다. 외부에서 접근불가
    def __init__(self):
        #self.insCount=self.insCount+1 ->self가 붙은것은 instance 영역이다
        CountManager.__insCount+=1
        #클래스 영역의 변수 값을 증가시킨다

    def staticprintCount():
        print("현재 객체 숫자", CountManager.__insCount)
        #위에 함수를 static으로 쓰려면 반드시 등록을 해야됨
    SprintCount = staticmethod(staticprintCount)

    #클래스메서드의 경우 첫번째 인자로 클래스가 전달된다
    def clsPrintCount(cls):
        print("현재 객체 숫자", cls.__insCount)
    clsPrintCount=classmethod(clsPrintCount)

a=[CountManager(), CountManager(), CountManager()]
CountManager.SprintCount()
a[0].SprintCount()
CountManager.clsPrintCount()
a[0].clsPrintCount()


class Util:
    def isCapital(c):
        if(ord('A')<=ord(c)<=ord('Z')):
            return True
        else:
            return False
    sPrint=staticmethod(isCapital)
    
    #전체문자열이 숫자로 구성되었는지 확인하기
    def isDigit(s):
        for c in s:
            if not ord('0')<=ord(c)<=ord('9'):  #이는 if ord('0')>ord(c) or ord(c)>ord('9')와 같다
                return False
        #for문을 다 빠져나오도록 return이 안되었다는 얘기는 다 숫자라는 것
        return True
    myIsDigit = staticmethod(isDigit)



print(Util.sPrint('A'))
print(Util.myIsDigit('1234'))
print(Util.myIsDigit('a1234'))

u=Util()   #이렇게 쓰면 불편하니까 위의 방식으로 씀
print(u.sPrint('B'))

