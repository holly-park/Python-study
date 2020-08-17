myList = [1,0,6,7,4,8,2,6,4,8,2,7,9,2,4,8,0,24,2435,23,3234]
print("크기: ", len(myList))
print(myList[0])
print(myList[3])
print(myList[5])
print(myList[2])
print(myList[4])
print(myList[6])
print(myList[-1])
print(myList[3:6])
print(myList[:7])

myWord=["ivy", "physics", "data", "osi", "variables", "notebook"]
print(myWord)
print(myWord[2])
print(myWord[2][0], myWord[2][1], myWord[2][2], myWord[2][3])
print(len(myWord[4]))

myWord[2] = "data science"
print(myWord)

myWord.append("gereme")
myWord.append("kokoko")
print(myWord)

myWord = myWord + ["jango"]
print(myWord)

#확장 - append와 달리 요소 하나씩이 아니라 list+list
myWord.extend("grapecandy") #string을 list로 전환시켜서
print(myWord)


del myWord[-1]
print("마지막요소 삭제하기: ", myWord)

#정렬하기
myWord.sort()
print(myWord)

#순서 리버스
myWord.reverse()
print(myWord)

#검색기능
print("위치값: ", myWord.index('gereme'))

print(myWord.count("python")) #존재하는 데이터 갯수
print("python" in myWord)  #true또는 false

#append: 맨뒤에
#insert: 중간에
myWord.insert(4,"fifc")
print(myWord)

myWord.remove("osi")
print(myWord)

#pop함수 : 맨 마지막 요소를 삭제한다
myWord.pop()
print(myWord)