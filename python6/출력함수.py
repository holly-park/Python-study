import sys
print("출력","연습", "pritn", sep="$", end="@")  #sep 분리
print("두번째줄", file=sys.stderr) #end에 줄바꿈을 안했기 때문에

f=open("파일출력.txt", "w", encoding="utf-8")   #엑셀: cp949
print("여기에 내보내는건 다 파일로 나감", file=f)
f.close()
