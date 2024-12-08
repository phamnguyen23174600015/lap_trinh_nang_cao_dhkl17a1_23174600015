import sqlite3

con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

cursor.execute("SELECT COUNT(*) FROM users")

count = cursor.fetchone()[0]
print(f"Tổng số bản ghi trong bảng 'users': {count}")
    



