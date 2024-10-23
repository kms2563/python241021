# import random
# print(random.random())



# lotto = random.sample(range(1,46),6)



# from os.path import *
# print(abspath("DemoOs.py"))
# print(basename("c:\\python310\\python.exe"))
# print(getsize("c:\\python310\\python.exe"))
# print(exists("c:\\python310\\python.exe"))


# fileName = "c:\\python310\\python.exe"
# if exists(fileName):
#     print("파일크기 : ", getsize(fileName))
# else:
#     print(f"{fileName} 파일이 존재하지 않습니다.")


# import os
# print("운영체제 이름:", os.name)
# print("운영체제 환경변수:", os.environ )

# 파일 목록 가져오기

import glob
# print(glob.glob("c:\\python310\\*.exe"))
lst = glob.glob(r"c:\\work\\*.py")
for item in lst:
    print(item)

