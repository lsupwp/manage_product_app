import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

file_path = os.getcwd()+os.getenv("DB_NAME")
with sqlite3.connect(file_path) as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                cost DECIMAL(10, 2) NOT NULL,
                barcode VARCHAR(50) UNIQUE NOT NULL
            );
        """
    )
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                total_amount DECIMAL(10, 2) NOT NULL,
                sale_time DATETIME NOT NULL
            );
        """
    )
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS SaleDetails (
                sale_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                sale_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                total_price DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (sale_id) REFERENCES Sales(sale_id),
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """
    )
    conn.commit()
print("สร้างฐานข้อมูลเรียบร้อยแล้ว")
