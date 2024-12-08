import sqlite3



con = sqlite3.connect('bai3.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bang1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    
con.commit()


print("Cơ sở dữ liệu và bảng 'bang1' đã được tạo thành công.")

con.close()

