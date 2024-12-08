import sqlite3


with sqlite3.connect("my.db") as conn:
    print(f"mở csdl sqlite với phiên bản {sqlite3.sqlite_version} thành công.")

