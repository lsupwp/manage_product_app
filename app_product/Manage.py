import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

class ManageProduct:

    def __init__(self):
        self.file_path = os.getcwd()+os.getenv("DB_NAME")
    
    def find_all(self):
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()

            data = cursor.execute(
                "SELECT * FROM Products"
            ).fetchall()
            return data  # Return the result
        
    def find_one(self, barcode: str):
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()

            data = cursor.execute(
                "SELECT * FROM Products WHERE barcode = ?",
                (barcode,)
            ).fetchall()
            return data  # Return the result

    def insert_product(self, name: str, price: int, cost: int, barcode: str):
        if len(name) <= 0:
            return {"status": "error", "msg": "กรุณากรอกชื่อสินค้าของคุณ"}
        if len(str(price)) <= 0:
            return {"status": "error", "msg": "กรุณากรอกราคาสินค้าของคุณ"}
        if len(str(cost)) <= 0:
            return {"status": "error", "msg": "กรุณากรอกต้นทุนสินค้าของท่าน"}
        if len(barcode) <= 0:
            return {"status": "error", "msg": "กรุณากรอกบาร์โค๊ดของสินค้า"}
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()
             
            data = cursor.execute(
                "SELECT * FROM Products WHERE barcode = ?",
                (barcode,)
            ).fetchall()  # Fetch the result directly

            if len(data) > 0:
                return {"status": "error", "msg": "สินค้านี้มีในระบบอยู่แล้ว"}
            
            cursor.execute(
                "INSERT INTO Products (name, price, cost, barcode) VALUES (?, ?, ?, ?)",
                (name, price, cost, barcode,)
            )
            conn.commit()
            return {"status": "success", "msg": "บันทึกสินค้าเรียบร้อยแล้ว"}
    
    def update_product(self, name: str, price: int, cost: int, barcode: str):
        if len(name) <= 0:
            return {"status": "error", "msg": "กรุณากรอกชื่อสินค้าของคุณ"}
        if len(str(price)) <= 0:
            return {"status": "error", "msg": "กรุณากรอกราคาสินค้าของคุณ"}
        if len(str(cost)) <= 0:
            return {"status": "error", "msg": "กรุณากรอกต้นทุนสินค้าของท่าน"}
        if len(barcode) <= 0:
            return {"status": "error", "msg": "กรุณากรอกบาร์โค๊ดของสินค้า"}
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()

            data = cursor.execute(
                "SELECT * FROM Products WHERE barcode = ?",
                (barcode,)
            ).fetchall()  # Fetch the result directly

            if len(data) > 0:
                cursor.execute(
                    "UPDATE Products SET name = ?, price = ?, cost = ?, barcode = ? WHERE barcode = ?",
                    (name, price, cost, barcode, barcode)
                )
                return {"status": "success", "msg": "แก้ไขข้อมูลสำเร็จ"}
            return {"status": "error", "msg": "ไม่มีสินค้านี้ในระบบ"}
        
    def delete_product(self, barcode: str):
        if len(barcode) <= 0:
            return {"status": "error", "msg": "กรุณากรอกบาร์โค๊ดของสินค้า"}
        with sqlite3.connect(self.file_path) as conn:
            cursor = conn.cursor()

            data = cursor.execute(
                "SELECT * FROM Products WHERE barcode = ?",
                (barcode,)
            ).fetchall()  # Fetch the result directly

            if len(data) > 0:
                cursor.execute(
                    "DELETE FROM Products WHERE barcode = ?",
                    (barcode,)
                )
                return {"status": "success", "msg": "ลบสินค้าสำเร็จ"}
            return {"status": "error", "msg": "ไม่มีสินค้านี้ในระบบ"}