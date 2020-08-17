class Animal:
    def __init__(self):
        print("Animal.__init__()")

class Tiger(Animal):
    def __init__(self):
        #Animal.__init__(self)라고 하면 Animal이 두번 호출되므로 super()로 수정
        #super뒤에는 self를 뺄 것
        super().__init__()
        print("Tiger__Init__")
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def cry(self):
        print("호랑이: 어흥")

class Lion(Animal):
    def __init__(self):
        #Animal.__init__(self)라고 하면 Animal이 두번 호출되므로 super()로 수정
        super().__init__()
        print("Lion__Init__")
    def Bite(self):
        print("사자처럼 한입에 꿀걱하기")
    def cry(self):
        print("사자: 으르렁")


class Liger(Tiger, Lion):
    def __init__(self):
        super().__init__()
        print("Liger __init__")
    def Play(self):
        print("라이거만의 사육사와 재미있게 놀기")

liger = Liger()
liger.Jump()
liger.Bite()
liger.Play()
liger.cry()