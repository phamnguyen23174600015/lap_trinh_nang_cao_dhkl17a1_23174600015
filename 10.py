import sqlite3

def them_sp(id, name, price, amount):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO san_pham (Id, Name, Price, Amount) 
    VALUES (?, ?, ?, ?)
    """, (id, name, price, amount))
    conn.commit()
    conn.close()
    print("Thêm sản phẩm thành công!")

def hien_thi():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM san_pham")
    products = cursor.fetchall()
    conn.close()
    print("Danh sách sản phẩm:")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Amount: {product[3]}")

def tim_kiem(name):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM san_pham WHERE name LIKE ?", (f"%{name}%",))
    products = cursor.fetchall()
    conn.close()
    if products:
        print("Kết quả tìm kiếm:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Amount: {product[3]}")
    else:
        print("Không tìm thấy sản phẩm nào.")

def cap_nhat(id, new_name, new_price, new_amount):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE san_pham 
    SET name = ?, price = ?, amount = ? 
    WHERE id = ?
    """, (new_name, new_price, new_amount, id))
    conn.commit()
    conn.close()
    print("Cập nhật sản phẩm thành công!")

def xoa(id):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM san_pham WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Xóa sản phẩm thành công!")

def menu():
    while True:
        print("\n=== Quản lý sản phẩm ===")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật tên, giá và số lượng sản phẩm")
        print("5. Xóa sản phẩm")
        print("0. Thoát")
        
        choice = int(input("Chọn chức năng: "))
        
        if choice == 1:
            hien_thi()
        elif choice == 2:
            id = int(input("Nhập ID: "))
            name = input("Tên sản phẩm: ")
            price = float(input("Giá: "))
            amount = int(input("Số lượng: "))
            them_sp(id, name, price, amount)
        elif choice == 3:
            name = input("Tên sản phẩm cần tìm: ")
            tim_kiem(name)
        elif choice == 4:
            id = int(input("ID sản phẩm cần cập nhật: "))
            new_name = input("Tên mới: ")
            new_price = float(input("Giá mới: "))
            new_amount = int(input("Số lượng mới: "))
            cap_nhat(id, new_name, new_price, new_amount)
        elif choice == 5:
            id = int(input("ID sản phẩm cần xóa: "))
            xoa(id)
        elif choice == 0:
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng không hợp lệ.")

# Chạy menu
menu()
