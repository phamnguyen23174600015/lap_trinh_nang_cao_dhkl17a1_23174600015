class Phan_so():
    def __init__(self):
        self.tu = int(input("Tử số: "))
        self.mau = self.check()

    def check(self):
        while True:
            mau = int(input("Mẫu số : "))
            if mau != 0:
                return mau
            else:
                print("Mẫu số không được bằng 0.")

phan_so = Phan_so()
print(f"Phân số: {phan_so.tu}/{phan_so.mau}")
