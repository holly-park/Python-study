#단어쪼개기
s = [
    "홍길동,42",
    "임꺽정,23",
    "장실산,34"
]

for ss in s:
    word=ss.split(",")
    print(word[0])
    print(word[1])
