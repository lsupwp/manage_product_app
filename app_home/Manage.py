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
        pass

    def insert_saleDetails(self, sale_id: int, product_id: int, quantity: int, price: float):
        pass