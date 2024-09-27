import math
class Tam_giac():
    def __init__(self):
        self.a = int(input("Nhập cạnh a"))
        self.b = int(input("Nhập cạnh b"))
        self.c = int(input("Nhập cạnh c "))
    
    def display(self):
        print(f"Tam giác có kích thước : {self.a}, {self.b}, {self.c}")

class Tam_giac_Can(Tam_giac):
    def __init__(self, a, b):
        super.__init__(a,a,b)

    def display(self):
        print(f"Tam giác cân với hai cạnh bằng nhau: {self.a}, cạnh đáy: {self.c}")

class Tam_giac_deu(Tam_giac_Can):
    def __init__(sel,a):
        super.__init__(a,a)

    def display(self):
        print(f"Tam giác đều có kích thước cánh là: {self.a}")

class Tam_giac_vuong(Tam_giac):
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)  
        super().__init__(a, b, c)

def main():
    while True:
        print("\nChọn hình:")
        print("1. tam giác")
        print("2. tam giác cân")
        print("3. tam giác đều")
        print("4. tam giác vuông")

        choice = input("Nhập lựa chọn của bạn (1-4): ")

        if choice == '1':
            tg = Tam_giac()
            tg.display()
        elif choice == '2':
            tgc = Tam_giac_Can()
            tgc.display()
        elif choice == '3':
            tgd = Tam_giac_deu()
            tgd.display()
        elif choice == '4':
            tgv = Tam_giac_vuong
            tgv.display()
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
