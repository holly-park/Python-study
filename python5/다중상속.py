class Tiger(Animal):
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def cry(self):
        print("호랑이: 어흥")

class Lion(Animal):
    def Bite(self):
        print("사자처럼 한입에 꿀걱하기")
    def cry(self):
        print("사자: 으르렁")


class Liger(Tiger, Lion):
    def Play(self):
        print("라이거만의 사육사와 재미있게 놀기")

liger = Liger()
liger.Jump()
liger.Bite()
liger.Play()
liger.cry()

