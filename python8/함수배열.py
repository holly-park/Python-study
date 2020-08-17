def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

#list에 함수 주소를 전달
functionList = [add, sub, mul, div]

#함수호출
print(functionList[0](4,5))

#이 함수를 쓰는 이유: for loop

for func in functionList:
    print(func(5,6))

for i in range(0, len(functionList)):
    print(functionList[i](6,2))

rList=[add(5,3),add(5,3),add(5,3),add(5,3)]
print(rList)


funcDict={}
funcDict["add"]=add
funcDict["sub"]=sub
funcDict["mul"]=mul
funcDict["div"]=div

fname = input("함수이름: ")
x = int(input("x = "))
y = int(input("y = "))

print(funcDict[fname](x,y))
