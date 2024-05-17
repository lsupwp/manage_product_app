import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

class ManageSell:
    
    def __init__(self) -> None:
        self.file_path = os.getcwd()+os.getenv("DB_NAME")

    def search_product(self, barcode: str):
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()
            data = cursor.execute(
                "SELECT * FROM Products WHERE barcode = ?",
                (barcode,)
            ).fetchall()
            return data

    def insert_sales(self, total_amount: float, sale_time: str):
        if len(str(total_amount)) <= 0:
            return {"status": "error", "msg": "total_amount has not found"}
        if len(str(sale_time)) <= 0:
            return {"status": "error", "msg": "sale_time has not found"}
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO Sales (total_amount, sale_time) VALUES (?, ?);",
                (total_amount, sale_time, )
            )
            conn.commit()
            return {"status": "success", "msg": "บันทึกข้อมูลสำเร็จ"}

    def insert_saleDetails(self, product_id: int, quantity: int, price: float):
        if len(str(product_id)) <= 0:
            return {"status": "error", "msg": "product_id has not found"}
        if len(str(quantity)) <= 0:
            return {"status": "error", "msg": "quantity has not found"}
        if len(str(price)) <= 0:
            return {"status": "error", "msg": "price has not found"}
        
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()

            data = cursor.execute(
                "SELECT sale_id FROM Sales ORDER BY sale_id DESC;"
            ).fetchone()

            sale_id = data[0]
            total_price = quantity * price
            cursor.execute(
                "INSERT INTO SaleDetails (sale_id, product_id, quantity, price, total_price) VALUES (?, ?, ?, ?, ?)",
                (sale_id, product_id, quantity, price,total_price,)
            )
            conn.commit()