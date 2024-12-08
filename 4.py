import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

if tables:
    print("Danh sách các bảng trong cơ sở dữ liệu:")
    for table in tables:
        print(f"- {table[0]}")
else:
    print("Không có bảng nào trong cơ sở dữ liệu.")
    

connection.close()


