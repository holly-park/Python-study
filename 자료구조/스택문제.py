"""
문제1. 스택을 사용해서 문자열을 뒤집어서 반환하는 함수
       s=reverse("korea")
       print(s) aerok
"""

# def reverse(a):
#     myList=list(a)
#     for i in a:
#         myList.append(i)
#     for i in myList:
#         s=myList.pop()

def reverse(data):
    stack = list()
    for c in data:
        stack.append(c)
    result=""
    while len(stack)!=0:
        result=result+stack.pop()
    return result

print(reverse("korea"))




