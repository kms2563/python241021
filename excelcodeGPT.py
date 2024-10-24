import openpyxl
from openpyxl import Workbook
import random

# 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "전자제품 판매 데이터"

# 헤더 추가
headers = ["제품ID", "제품명", "수량", "가격"]
ws.append(headers)

# 제품명 리스트
products = ["스마트폰", "노트북", "태블릿", "스마트워치", "이어폰", "스피커", "TV", "냉장고", "세탁기", "에어컨"]

# 100개의 데이터 생성 및 추가
for i in range(1, 101):
    product_id = f"P{i:03d}"
    product_name = random.choice(products)
    quantity = random.randint(1, 100)
    price = random.randint(10000, 2000000)
    
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")

print("products.xlsx 파일이 생성되었습니다.")