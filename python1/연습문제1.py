#홍길동의 과목별 평균은?
kor = 80
eng = 75
mat = 55
avg = (kor+eng+mat)/3
print("홍길동의 평균은 {}점 입니다".format(avg))

#홍길동의 주민등록번호를 앞자리와 뒷자리로 쪼개는 법
idn = [8,8,1,1,2,0,1,0,6,8,2,3,4]
print("홍길동의 주민번호 앞자리는 {} 입니다".format(idn[0:6]))
print("홍길동의 주민번호 앞자리는 {} 입니다".format(idn[6:]))

#a:b:c:d를 replace함수를 이용하여 a#b#c#d로 바꿔라
r = "a:b:c:d"
p=r.replace(":","#")
print(p)

#[1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
myList = [1,3,5,4,2]
myList.sort()
myList.reverse()
print(myList)

#(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)
myTuple=(1,2,3)
myTuple=myTuple+(4,)
print(myTuple)

#a = {'A':90, 'B':80, 'C':70}에서 B의 값 추출하기
myDic={'A':90, 'B':80, 'C':70}
print(myDic.get('B'))

#a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5] 중복제거
a=[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
sett=set([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5])
print(sett)

#위의 문제 다시하기
a=[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet=set(a)
print(aSet)

