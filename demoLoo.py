lst  = [100,200,300]

for item in lst:
    print(item)


print("==range()==")
print(list(range(10)))
print(list(range(2000,2025)))
print(list(range(1,32)))



list("--리스트 내장 ---")
lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i>5])


tp = ("apple", "orrange", "kiwi")
print([len(i) for i in tp])

d = {100:"apple", 200:"orange"}
print([v.upper() for v in d.values()])


print("--filtering function --")

lst = [10,25,30]
itemL = filter(None,lst)
for i in itemL:
    print("item:{0}".format(i))

def getbiggerthan20(i):
    return i>20

print("==f==")
itemL = filter(getbiggerthan20,lst)
for i in itemL:
    print("item:{0}".format(i))



print("==lambda==")
itemL = filter(lambda x: x>27,lst)
for i in itemL:
    print("item:{0}".format(i))


