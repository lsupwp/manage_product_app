import os
from dotenv import load_dotenv

load_dotenv()

# ใช้ os.path.realpath(__file__) เพื่อหา path ของไฟล์ปัจจุบัน
current_file_path = os.path.realpath(__file__)
print("Path ของไฟล์ปัจจุบัน:", current_file_path)

# หรือใช้ os.getcwd() เพื่อหา path ของไดเรกทอรีปัจจุบัน
current_directory = os.getcwd()+os.getenv("DB_NAME")
print("ไดเรกทอรีปัจจุบัน:", current_directory)
