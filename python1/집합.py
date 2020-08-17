pleomax = set([1,4,5,6,7,23])
lesum = set([3,5,6,7,23])
print(type(pleomax))

#교집합 구하기
gyo = pleomax.intersection(lesum)
print(gyo)

#합집합
hap = pleomax.union(lesum)
print(hap)

#차집합
cha = pleomax.difference(lesum)
print(cha)

myWater=set([1,2,3,3,4,4,4,5,6,6,7])
print(myWater)
#print(myWater[0]) - 집합은 인덱싱을 지원하지 않는다
myWaterList = list(myWater)
#집합을 list타입으로 전환하면 indexing 가능하다
print(myWaterList)
print(type(myWaterList))
