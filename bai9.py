class da_giac():
    def __init__(self, canh):
        self.canh = canh

    def display(self):
        print(f"đa giác có {self.canh} cạnh ")

class hinh_binh_hanh(da_giac):
    def __init__(self):
        super().__init__(4)  
        self.day = float(input("Nhập cạnh đáy: "))  
        self.canh = float(input("Nhập cạnh bên: "))  
        self.cao = float(input("Nhập chiều cao: "))  

    def dien_tich(self):
        return self.day * self.cao
    
    def chu_vi(self):
        return 2 * (self.day * self.canh)
    

    def display(self):
        print(f"Hình bình hành: Cạnh đáy = {self.day}, Cạnh bên = {self.canh}, Chiều cao = {self.cao}")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")
    
class hinh_chu_nhat(hinh_binh_hanh):
    def __init__(self):
        super().__init__()
        self.dai = self.canh 
        self.rong = self.canh 

    def display(self):
        print(f"Hình chữ nhật: Chiều dài = {self.dai}, Chiều rộng = {self.rong}")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")

class hinh_vuong(hinh_chu_nhat):
    def __init__(self):
        self.canh = float(input("Nhập cạnh hình vuông: "))  
        super().__init__()  

    def dien_tich(self):
        return self.canh * self.canh

    def chu_vi(self):
        return 4 * self.canh

    def display(self):
        print(f"Hình vuông: Cạnh = {self.canh}")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")


def main():
    while True:
        print("\nChọn hình để tính toán:")
        print("1. Hình bình hành")
        print("2. Hình chữ nhật")
        print("3. Hình vuông")
        print("4. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-4): ")

        if choice == '1':
            parallelogram = hinh_binh_hanh()
            parallelogram.display()
        elif choice == '2':
            rectangle = hinh_chu_nhat()
            rectangle.display()
        elif choice == '3':
            square = hinh_vuong()
            square.display()
        elif choice == '4':
            print("Thoát chương trình.")
        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


if __name__ == "__main__":
    main()