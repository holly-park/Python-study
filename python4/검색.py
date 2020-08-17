x=["flower", "rain", "cloud","rain","hope","chair"]
y=["fruits", "orange", "rain", "chair", "chair"]

#두개의 리스트에서 공통된 것을 찾아내기
commonList=[] #이때 객체가 만들어진다
for word in x:
    print(word)
    if word in y and word not in commonList:
         #y리스트에 word가 존재하느냐
         #commonList에 존재하지 않느냐(중복제거)
        commonList.append(word)

print(commonList)
