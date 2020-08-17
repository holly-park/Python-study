"""
선형검색: 처음부터 순차적으로 데이터를 읽는다
List에 데이터가 들어가 있어야 메모리 비교가 되서 정렬 또는 검색을 할 수 있다
데이터가 많으면 속도가 엄청 느리다
이분검색: 데이터가 순서대로 정렬되어 있어야 한다
          중간을 기준으로 나누어서 키 값이 속해있는 그룹을 선택하고
         나머지 버림. 이것을 반복
"""

a=[1,2,3,4,5,6,7,8,9,10]
key=4
if key in a:
    print(a.index(key))
else:
    print("없다")



if a.count(key) !=0:
    print(a.index(key))
else:
    print("없다")

words = ["커피", "옥수수차", "녹차", "밀크티", "홍차"]
if  "옥수수차" in words:
    print("존재함")
else:
    print("없음")

words = {'school':'학교'}
words['hospital']="병원"
words['survey']="조사하다"
words['president']="대통령"
words['assembly']="국회"
words['government']="정부"

key="survey"
if key in words:
    print(words[key])
else:
    print("없다")


s="""
I like star
red star
yello star
green star

I like star
"""
print("star", s.count("star"))
print("like", s.count("like"))
print("green", s.count("green"))
print("you", s.count("you"))