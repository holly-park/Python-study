class Mytype:
    def __init__(self, r=1, i=1):
        self.r=r
        self.i=i
    def print(self):
        print("{}+{}i".format(self.r, self.i))

    #t1+t2
    def __add__(self, other):
        temp = Mytype()
        temp.r = self.r+other.r
        temp.i = self.i+other.i
        return temp

    def __sub__(self, other):
        temp = Mytype()
        temp.r = self.r-other.r
        temp.i = self.i-other.i
        return temp


t1 = Mytype(2,3)
t2 = Mytype(4,5)
t1.print()
t2.print()

t3 = t1 + t2
t3.print()

t4 = t1 - t2
t4.print()