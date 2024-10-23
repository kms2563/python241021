#db1.py             

import sqlite3

#일단 메모리에서 연습
con = sqlite3.connect(r"c:\work\sample.db")

#커서 인스턴스 생성
cur = con.cursor()

# 테이블 구조 생성

cur.execute("create table if not exists PhoneBook (Name text, PhoneNum Text);")

#1건 데이터 입력
cur.execute("INSERT into PhoneBook values ('derick', '010-1111-1111') ; ")
name = "홍길동"
phoneNumber = "010-123-6663"
cur.execute("INSERT into Phonebook values (?, ?)", (name, phoneNumber))

#여러건을 입력
datalist = (("이순신", "010-222-2222"), ("박지성", "010-333-3333"))
cur.executemany("INSERT into Phonebook values (?, ?)", datalist)  # 여러번 수행해라

#데이터 조회
cur.execute("SELECT * FROM Phonebook")



#입력된것을 확인하고나서 commit()을 반드시 해야함..............
con.commit() # 완료 하는 것임.!!!

#일단 메모리에서 연습
#영구적으로 파일에 저장


for row in cur:
    print(row)
print(cur.fetchall())
