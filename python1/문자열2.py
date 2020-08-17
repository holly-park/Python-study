s="Life is too short, You need Python"
print("문자열의 길이: ", len(s))

a=[1,2,3,4]
print("a의 길이: ", len(a))

#indexing
print("첫번째 문자: ", s[0])
print("마지막 문자: ", s[-1])


#slicing
print(s[0:4]) #0,1,2,3 마지막은 뺀다
print(s[:12]) #0,1,2,3,4,5,6,7,8,9,10,11
print(s[12:]) #12이후로 끝까지

#s[0]='1' #값 바꾸기 불가
s2='1' + s[1:]
print(s2)

# %d - decimal(10진수)
b = "I eat %d apples and %d peaches." %(3,5) 
print(b)

c = "I eat {} apples and {} peaches.".format(3,5) 
print(c)

d = "문자열: %s 정수: %d %o %x 실수: %f " % ("test",15,10,5,4.5)
print(d)

e = "실수: %.2f%% " %(4.5)
print(e)

f = "정수: %05d" %(15)
print(f)

g = "0:{2} 1:{1} 2:{0} {1}".format(3,4,5) 
print(g)

k = "%-20s*" % ('korea')
print(k)
kk = "%20s*" % ('korea')
print(kk)

lol = "I already had {number} cups of coffee today".format(number=5)
print(lol)


print("{0:10}".format(15))
print("{:>10}".format(15))  #왼쪽정렬
print("{:<10}".format(15))  #오른쪽정렬
print("{:^10}".format(15))  #가운데정렬
print("{:>010}".format(15)) #빈자리 0으로 채움