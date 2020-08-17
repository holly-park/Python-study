"""함수만들기, 문자열, 문자 "I like star, red star","s"
print(mycount("I like star, red star", "s"))
s가 몇번 등장했는지 숫자 반환함수
"""

def mycount(sentence, mark):
    count=0
    for c in sentence:
        if c==mark:
            count +=1
    return count

print(mycount("I like star, red star", "s"))