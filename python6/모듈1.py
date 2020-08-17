import math  #외부의 파일을 이 파일안으로 들고들어와라

print(math.pow(2,10))
print(math.pi)

from ftplib import FTP  #FTP클라이언트 모듈

ftp = FTP("ftp1.at.proftpd.org")
print(ftp.login())  #로그인 요청
print(ftp.retrlines('LIST'))  #list는 목록을 보는 명령어
print(ftp.quit())
