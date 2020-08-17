for x in range(1,10):
    print(str(x).ljust(3), "x", x, "=", str(x*x).rjust(5))  #string타입을 정렬가능

w=["house","dog","cat","hospital","president"]
for word in w:
    print(word.rjust(20))
for word in w:
    print("*",word.center(20),"*")

dic=[{"item":"apple", "color":"red"}]
print("{0[item]} is {0[color]}".format(dic[1]))

for item in dic:
    print("{0} is {1}".format(item["item"], item["color"]))