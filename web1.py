# web1.py
# 웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

#웹페이지를 로딩

page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#html 파서 : "상수값을 지정"
soup = BeautifulSoup(page, "html.parser")

#원하는 데이터 추출
# print(soup.find_all("p"))

#첫번재 <p> 태그 추출
print(soup.find("p"))

# print(soup.prettify())
# 조건 검색 : <p class="outer-text">
print(soup.find_all("p", class_="outer-text")) 
#find인데 너무 많음 :outer-text 

print(soup.find_all("p", attrs={"class":"outer-text"}))
# 조건 검색 클래스는  outer-text 인데 attributes를 잘 해보기

#태그 내부 문자열 추출
for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)

#태그를 없애버리니까 줄 바꿈 문자들이 남는다
# 그러니까 줄바꿈 문자를 없애주는 것이 좋다
print("========================")
for tag in soup.find_all("p"):
    title = tag.text.replace("\n", "")
    print(title)


# id로 검색
print(soup.find(id="first"))


#