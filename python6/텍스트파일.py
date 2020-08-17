f=open("test2.txt", "w")  #파일을 쓰기모드로 연다
f.write("file write test\n")
f.write("file write test 2222\n")
f.write("file write test 333")
f.close()

f=open("test2.txt", "r")
s=f.read()
print(s)
print(type(s))
f.close()

f=open("test2.txt", "r")
sList = f.readlines()
print(type(sList))
for line in sList:
    print(line, end="")
f.close()