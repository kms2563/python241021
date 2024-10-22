# class 1.py
# 클래스의 정의
class person: 
    # 초기화 메서드
    def __init__(self):
        self.name = "default name"
        
    def print(self):
        print("My name is {0}".format(self.name))


# 인스터스 생성
        
p1 = person()
p2 = person()
p1.print()
p1.name = "abc"
p1.print()
p2.name = "gabriel"
p2.print()

#  whtlagodi gkf rjt


strName = " 전역변수의 값"
class DemoString:
    def __init__(self):
        self.strName = ""

    












