#약간 더 복잡한 함수
#합집합 함수

def union(*ar):  # *은 튜플이라는 의미이다. 포인터 아니다 튜플로 받는다.
    result = [] # 리스트, 지역변수
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result



print(union("HAM","EGG",))
print(union("HAM","EGG","SPAM"))

g = lambda x,y:x+y
print(g(1,2))
print(g(3,4))
print((lambda x:x*x)(2**5))
print(globals())
print(dir())

value = 5
while value>0:
    print(value)
    value -=1



# for <타겟> in <객체>
lst = ["apple",100,3.14]
for item in lst:
    print(item,type(item))