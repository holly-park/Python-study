a=list(range(1,11))
#리스트 내장을 이용해서 홀수만 추출하기

b= [i for i in a if i%2==1]
print(b)

words=["bread","coffee","toast","ricecake","cake","soup"]
words2=[w.upper() for w in words]
print(words2)

sentence="".join(words)
print(sentence)
