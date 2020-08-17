for i in range(1,11):
    for j in range(1,11):
        print(i, j)
        if j==5:
            break  #가장 가까운 블록만 빠져나감

for j in range(1,11):
    if j==5:
        continue
    print(j)
else:  #위에서 continue와 break가 실행되지 않았을 때 else구문이 실행
    print("break나 continue구문이 실행되지 않았습니다.")


#검색
a=[1,2,3,5,8,12,13,54,66,77]
key= 66
for i in a:
    if key ==i:
        print("찾음")
        break
else:
    print("못찾음")