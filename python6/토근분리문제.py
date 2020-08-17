"""
김정하,90,90,80
이민주,80,80,70
조승연,90,100,90

이 데이터로 성적의 총점과 평균 구하기
"""

f=open("data.txt","r", encoding="utf-8") 
sList=f.readlines()
f.close()

total=0
cnt=0
for item in sList:
     if item!= "\n":
        data=item.split(",")
        name=data[0]
        kor=int(data[1])
        eng=int(data[2])
        mat=int(data[3])
        total=kor+eng+mat
        avg=total/3
        print(name, kor, eng, mat, total, avg)   








