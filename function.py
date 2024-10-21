#function.py

# 함수를 정의

def times(a,b):
    return a*b

result = times(4,6)
print(result)



def setValue(newValue):
    x = newValue
    print("함수내부 :  ",  x)


result = setValue(5)
print(result)


print("=========")


# 전역변수와 지역변수
x = 5 # 전역변수
def func(a):
    return x+a

def func1(a):
    x=1 # 지역변수
    return x+a

print(func(1))
print(func1(1))

def times(a=10,b=20):
    return a*b
print("========")
print(times())
print(times(5))
print(times(b=5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http:\\"+server + ":"+ port
    return strURL

print(connectURI("yahoo.com","8080"))
print(connectURI(port = "40", server = 'naver.com'))

# 가변인자






#람다 함수 람다는 1회용으로 쓰고 버릴것이다. 입력 데이터 받아서 프로세싱하고 
#람다 모양 lamda x,y : x*y 이게 간결한 표현식인데 앞에 2개 받고 뒤에 x*y는 return 한다!















