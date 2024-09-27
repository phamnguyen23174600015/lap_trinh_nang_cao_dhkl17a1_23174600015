class Hcn():
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0
    def vao(self):
        self.chieu_dai = int(input("nhập chiều dài: "))
        self.chieu_rong = int(input("Chiều rộng: "))
    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def ra(self):
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")

hcn = Hcn()
hcn.vao()
hcn.ra()
