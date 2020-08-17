filePath="./text.txt"       # . =>현재 프로그램이 작동중인 경로
try:
    f=open(filePath, "r", encoding="utf-8")   #읽기모드로 파일을 연다
    try:
        data=f.read(128)    #최대 128 byte를 읽어라
        print(data)
    except Exception as e:
        print(e.args[0])
    finally:
        f.close()           #만약 예외가 발생하더라도 파일을 닫는다
except IOError:
    print(filePath + "is not found")
