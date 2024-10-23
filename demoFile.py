#파일을 쓰기
f = open("demo.txt", "wt", encoding="utf-8")
f.write("Hello, World!\n")

f.close()

f=open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.close()



# print(dir(str))
data = "<<<   I don't like SPAM   >>>>"
result = data.strip("<> ")
print(result)
print(data)


print("MBC2580".isalnum())
print("MBC2580".isalpha())
print("2580".isdigit())
print("2580".isdecimal())
print("2580".isnumeric())
print("2580".isspace())
print("2580".isupper())
print("2580".islower())
print("2580".istitle())









# 정규표현식

# chat GPT가 잘 짜준다
'''
# ^app로 시작하는것만 가져와
ful$ 은 ful로 끝나는것만 가져와
[] 정규 표현식은 
| 짝대기 연산다 A또는 B를 나타낸다.
\s 는 공백문자를 나타낸다.
\d 는 숫자를 나타낸다.
\w 는 문자를 나타낸다.
\b 는 단어의 경계를 나타낸다.
\B 는 단어의 경계가 아닌 것을 나타낸다.

re.search() 는 문자열 전체를 검색해 처음으로 매칭되는 패턴을 찾는다.
re.match() 는 문자열의 처음부터 패턴을 검색해 매칭되는 패턴을 찾는다.
re.findall() 은 문자열 전체에서 패턴과 매칭되는 모든 문자열을 찾아 리스트로 반환한다.
re.sub() 는 문자열에서 패턴과 매칭되는 문자열을 찾아 다른 문자열로 대체한다.
re.compile() 은 패턴을 정규 표현식 객체로 만든다.               


'''