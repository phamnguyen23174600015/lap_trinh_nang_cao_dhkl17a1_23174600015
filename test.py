import sqlite3

def add_product(id, name, price, amount):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO product (id, name, price, amount) 
    VALUES (?, ?, ?, ?)
    """, (id, name, price, amount))
    conn.commit()
    conn.close()
    print("Thêm sản phẩm thành công!")

# Gọi hàm để thêm sản phẩm
add_product(1, "Laptop", 1500.0, 10)
add_product(2, "Smartphone", 800.0, 20)



def update_product(id, new_price, new_amount):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE product 
    SET price = ?, amount = ? 
    WHERE id = ?
    """, (new_price, new_amount, id))
    conn.commit()
    conn.close()
    print("Cập nhật sản phẩm thành công!")

# Gọi hàm cập nhật
update_product(1, 1600.0, 15)
