import sqlite3
import random

class GroceryManager:
    def __init__(self, db_name='grocery.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS groceries (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert(self, name, price):
        self.cursor.execute('INSERT INTO groceries (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, id, name=None, price=None):
        if name and price:
            self.cursor.execute('UPDATE groceries SET name = ?, price = ? WHERE id = ?', (name, price, id))
        elif name:
            self.cursor.execute('UPDATE groceries SET name = ? WHERE id = ?', (name, id))
        elif price:
            self.cursor.execute('UPDATE groceries SET price = ? WHERE id = ?', (price, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM groceries WHERE id = ?', (id,))
        self.conn.commit()

    def select(self, id=None):
        if id:
            self.cursor.execute('SELECT * FROM groceries WHERE id = ?', (id,))
            return self.cursor.fetchone()
        else:
            self.cursor.execute('SELECT * FROM groceries')
            return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# 샘플 데이터 생성 및 삽입
def create_sample_data(manager):
    groceries = [
        "사과", "바나나", "오렌지", "우유", "빵", "계란", "치즈", "요구르트", "토마토", "감자",
        "양파", "당근", "브로콜리", "시리얼", "쌀", "파스타", "올리브 오일", "소금", "설탕", "커피"
    ]

    for _ in range(100):
        name = random.choice(groceries)
        price = round(random.uniform(1000, 20000), -2)  # 1000원에서 20000원 사이, 100원 단위로 반올림
        manager.insert(name, price)

# 사용 예시
if __name__ == "__main__":
    manager = GroceryManager()
    create_sample_data(manager)

    print("전체 데이터:")
    for item in manager.select():
        print(item)

    print("\n특정 항목 조회 (ID=5):")
    print(manager.select(5))

    print("\n항목 업데이트 (ID=5, 새 가격=15000):")
    manager.update(5, price=15000)
    print(manager.select(5))

    print("\n항목 삭제 (ID=10):")
    manager.delete(10)
    print(manager.select(10))

    manager.close()