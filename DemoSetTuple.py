#DemoSetTuple.py

#세트형식
a = {1,2,3,3,3}
b = {3,4,4,4,5}


print(a)
print(b)
print("중복은 스스로 제거한다")
print(type(a))
print(a.union(b))  # 합집합
print(a.intersection(b)) # 교집합
print(a.difference(b)) # 차집합
print("============")

tp = (10,20,30)
print(len(tp))
print(type(tp))

print("============")
def calc(a,b):
    return a+b, a*b

result= calc(3,4)
print(result[0])
print(result[1])

strA = "김유신"
strB = "홍길동"
print("id : %s , name : %s ",strA,strB)

# 형식을 변환 (Type Casting)

a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
#c.append(5) #  튜플에서 append 불가
print(c)

#딕셔너리, Dict , 순서가 정해져 있지 않다. 순서를 보장해주지 않는다. 딕셔너리는 키중심 앞에가 중심이다. Key, Value 형태로 이루어짐
#키를 가지고 입력 추가 삭제가 가능하다. 순서가 보정되는건 리스트
#세트나 딕셔너리는 순서가 보장되지 않기때문에 반드시 키를 가지고 값을 뽑아내고 인덱싱 한다.
# items = Key+Value를 포함하는것 .keys는 키만 리턴함 .   values()는 value만 리턴한다.
# color
# '


#  딕셔너리
colors = {"apple" : "red", "banana" : "yellow", "mango" : "yellow"}

print(colors)


colors["cherry"] = "red"
print(colors)

print("======")
del colors["mango"]
for item in colors.items():
    print(item)
print("=======")
for k,v in colors.items(): #변수 두개로 받는것이다. !!!!!!
    print(k,v)

# bool ?????????   true=>True, false = False None = null 비어있음,접근하지마
# NAN = not an Number 결측치!! nan과 null
# bool 은 0이 아니면 True다
# / 한번쓰면 실수를 받는다. //는 정수만 받는다.
#bool({1.2.3.4})


isRight=False
isTrue= True
print(type(isRight))
print(type(isTrue))
print("-0-000")
print(1<2)
print(1 == 2 )
print( 1 != 2)
print(True or True or False)
print(True and False and True)




print(5/2)
print(5//2)
print(5%2)
print(4%2)
print(7%5)
print(7%4)


# 함수의 정의, 함수도 객체처럼 메모리상에 생성된다.
# def = define 정의한다! 
# def <함수명>(인자1,인자2,.....)


globals()

# 참조만 복사??? pass by reference 참조가 대입이 되면  Mytimes = times 에서 "="는 값을 복사하는게 아니라 주소를 복사한다??? 
# 레퍼런스를 복사한다. 

# 실제 함수를 정의하고







    












