# 부모클래스 정의

class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스 정의
class Student(Person):

    def __init__(self, name, phoneNumber, subject, studentID): # 덮어쓰기(재정의, override)
        #명시적으로 부모화 메소드 호출
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("자식")
        print("(이름:{0}, 휴대폰번호: {1})".format(self.name, self.phoneNumber))
        print("(학과:{0}, 학번: {1})".format(self.subject, self.studentID))

# 인스턴스 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "인공지능학과", "2400000")


p.printInfo()
s.printInfo()





