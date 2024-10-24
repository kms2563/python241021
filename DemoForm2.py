# DemoForm2.py

# Demoform2.ui(화면단) + DemoForm2.py(로직단)
# 웹크롤링에 관한 선언
# 

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import requests


#미리 디자인한 문서를 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#DemoForm 클래스 정의 (QmainWindow 상속)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
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
        self.label.setText("당근마켓 크롤링 완료")

     

    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭했습니다.")

#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()

