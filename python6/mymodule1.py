def sigma(limit):
    s=0
    for i in range(1, limit+1):
        s=s+i
    return s

def gugudan(dan):
    for i in range(1,10):
        print("{} x {} ={}".format(dan, i, dan*i))

print(__name__)
if __name__ == "__main__":
    print(sigma(100))
    gugudan(5)