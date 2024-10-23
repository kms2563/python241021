#web2.py
# 웹크롤링에 관한 선언
# 
from bs4 import BeautifulSoup

import requests

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

#검색이 용이한 객체 생성
soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", attrs={"class":"card-desc"})

f = open("daangn.txt", "a+", encoding="utf-8")
for post in posts:
    titleElement = post.find("h2", attrs={"class":"card-title"})
    priceElement = post.find("div", attrs={"class":"card-price"})
    regionElement = post.find("div", attrs={"class":"card-region-name"})
    title = titleElement.text.replace("\n", "").strip()
    price = priceElement.text.replace("\n", "").strip()
    region = regionElement.text.replace("\n", "").strip()
    #내부에 문자열만 출력:f-string

    # print(f"{titleElement.text}, {priceElement.text}, {regionElement.text}")
    print(f"{title}, {price}, {region}")
    f.write(f"{title}, {price}, {region}\n")
    
f.close()   
#웹페이지 수소

    # <div class="card-desc">
    #   <h2 class="card-title">호박 고구마10k</h2>
    #   <div class="card-price ">
    #     9,000원
    #   </div>
    #   <div class="card-region-name">
    #     서울 중랑구 면목동
    #   </div>
# 
# 
# 
# 
#     