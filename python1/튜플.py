a=(1,2,3)
print(type(a))
print(a)

a=("문자", 3, 4)
print(type(a))
print(a)
a,b,c=(1,2,3)
print(a)
print(b)
print(c)
print(type(a))


x=10
y=20
z=x
x=y
y=z
print(x,y)

a,b = b,a
print("a=", a)
print("b=", b)

def myfunc(a,b,c):
    a=a*2
    b=b*2
    c=c*2
    return(a,b,c)

x,y,z=myfunc(10,20,30)
print(x,y,z)