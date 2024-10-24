import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# 외부 라이브러리 선언

class ProductDatabase:
    def __init__(self, db_name="ProductList.db"):
        self.db_name = db_name
        self._connect()

    def _connect(self):
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        if not os.path.exists(self.db_name):
            self.cur.execute(
                "create table if not exists Products (id integer primary key, Name text, Price integer);"
            )
            self.con.commit()

    def add_product(self, product_id, name, price):
        self.cur.execute("insert into Products (id, Name, Price) values(?, ?, ?);", (product_id, name, price))
        self.con.commit()

    def update_product(self, product_id, name, price):
        self.cur.execute("update Products set name=?, price=? where id=?;", (name, price, product_id))
        self.con.commit()

    def remove_product(self, product_id):
        self.cur.execute("delete from Products where id=?;", (product_id,))
        self.con.commit()

    def get_all_products(self):
        self.cur.execute("select * from Products;")
        return self.cur.fetchall()


# 디자인 파일을 로딩
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]


class DemoForm(QMainWindow, form_class):
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        self.db = db

        # 초기값 셋팅
        self.id = 0
        self.name = ""
        self.price = 0

        # QTableWidget의 컬럼폭 셋팅하기
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        # QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        # QTableWidget의 컬럼 정렬하기

        # self.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        # self.tableWidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        # 탭키로 네비게이션 금지
        self.tableWidget.setTabKeyNavigation(False)
        # 엔터키를 클릭하면 다음 컨트롤로 이동하는 경우
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 버튼 연결
        self.pushButton.clicked.connect(self.addProduct)
        self.pushButton_2.clicked.connect(self.updateProduct)
        self.pushButton_3.clicked.connect(self.getProduct)
        self.pushButton_4.clicked.connect(self.removeProduct)

    def addProduct(self):
        # 입력 파라메터 처리
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        self.db.add_product(self.id, self.name, self.price)
        # 리프레시
        self.getProduct()

    def updateProduct(self):
        # 업데이트 작업시 파라메터 처리
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        self.db.update_product(self.id, self.name, self.price)
        # 리프레시
        self.getProduct()

    def removeProduct(self):
        # 삭제 파라메터 처리
        self.id = self.prodID.text()
        self.db.remove_product(self.id)
        # 리프레시
        self.getProduct()

    def getProduct(self):
        # 검색 결과를 보여주기전에 기존 컨텐트를 삭제(헤더는 제외)
        self.tableWidget.clearContents()
        products = self.db.get_all_products()

        # 행숫자 카운트
        row = 0
        for item in products:
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])

            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다.
            itemID = QTableWidgetItem(int_as_strID)
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)

            # 제품명은 그대로 출력한다.
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다.
            itemPrice = QTableWidgetItem(int_as_strPrice)
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

            row += 1
            print("row: ", row)

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = ProductDatabase()
    demoForm = DemoForm(db)
    demoForm.show()
    app.exec_()
