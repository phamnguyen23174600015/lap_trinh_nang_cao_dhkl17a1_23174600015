import math

class diem:
    def __init__(self, x= 0, y = 0):
        self.x = x
        self.y = y

    def display(self):
        return f"Tọa độ của điểm: ({self.x}, {self.y})"

class Elip(diem):
    def __init__(self, x=0, y=0, a=1, b=1):
        super().__init__(x, y)  
        self.a = a  
        self.b = b  

    def dt(self):
        return math.pi * self.a * self.b

    def display(self):
        return f"Elip tại {super().display()} với bán trục lớn {self.a} và bán trục nhỏ {self.b}"

class hinh_tron(Elip):
    def __init__(self, x=0, y=0, ban_kinh=1):
        super().__init__(x, y, ban_kinh, ban_kinh)  
        self.ban_kinh = ban_kinh

    def dt(self):
        return math.pi * self.ban_kinh ** 2

    def display(self):
        return f"Đường tròn tại {super().display()} với bán kính {self.ban_kinh}"




x = float(input("Nhập tọa độ x của tâm elip: "))
y = float(input("Nhập tọa độ y của tâm elip: "))
a = float(input("Nhập bán trục lớn a của elip: "))
b = float(input("Nhập bán trục nhỏ b của elip: "))

elip = Elip(x, y, a, b)
print(elip.display())
print(f"Diện tích của elip: {elip.dt()}")


bk = float(input("Nhập bán kính của đường tròn: "))
circle = hinh_tron(x, y, bk)
print(circle.display())
print(f"Diện tích của đường tròn: {circle.dt()}")
