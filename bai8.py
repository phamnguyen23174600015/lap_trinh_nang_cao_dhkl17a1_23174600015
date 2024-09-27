class Date():
    def __init__(self):
        self.day = int(input("Ngày: "))
        self.month = int(input("Tháng: "))
        self.year = int(input("Năm: "))

    def display(self):
        print("Ngày", self.day, "tháng", self.month, "năm", self.year)

class employed:
    def __init__(self):
        self.ten = input("Nhập tên: ")
        print("Nhập ngày sinh: ")
        self.ngay_sinh = Date()
        print("Nhập ngày vào:")
        self.ngay_vao = Date()

    def display(self):
        print(f"Tên: {self.ten}")
        print("Ngày sinh:", end=" ")
        self.ngay_sinh.display() 
        print("Ngày vào công ty:", end=" ")
        self.ngay_vao.display()
        
def main():
    ds_nhan_su = []
    while True:
        print("\nChương trình quản lý nhân viên:")
        print("1. Thêm nhân viên")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-3): ")

        if choice == '1':
            employee = employed() 
            ds_nhan_su.append(employee)  
        elif choice == '2':
            if not ds_nhan_su:
                print("Hiện không có nhân viên nào.")
            else:
                idx = 1
                for nhan_su in ds_nhan_su:
                    print(f"\nNhân viên {idx}:")
                    employee.display()
                    idx += 1  
        elif choice == '3':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


if __name__ == "__main__":
    main()

