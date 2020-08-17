for item in ['커피', '요거트', '스무디', '샤베트', '아이스크림']:
   print(item) #리스트

for item in ('하루', '이틀', '사흘', '나흘', '닷새'):
    print(item) #튜플

colors = {'red': 'apple', 'yello':'papaya', 'green':'kiwi', 'brown':'mola'}
for item in colors:
    print(item) #딕션너리
    #키 값이 출력됨
    print(item, "===>", colors[item]) #dictionary를 모조리 출력하고 할 때

#배열의 인덱스와 내용을 동시에
drinks=["yogurt", "coffeee", "fruits juice", "milk"]
for index, value in enumerate(drinks):
    print(index, value) # 튜플로 옴