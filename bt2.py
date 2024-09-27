class quan_li():
    def __init__(self):
        self.name = input("Tên: ")
        self.toan = int(input("điểm toán: "))
        self.li = int(input("điểm lí: "))
        self.hoa = int(input("điểm hóa: "))

    def tong_diem(self):
        return self.toan + self.hoa + self.li
    
    def tra_thong_tin(self):
        print(f"Tên: {self.name}, Tổng điểm: {self.tong_diem()}")
    
    @staticmethod
    def trung_tuyen(ds):
        ds_trung = [trung_tuyen for trung_tuyen in ds if trung_tuyen.tong_diem() >= 20]
        return ds_trung

ds = []

for _ in range(5):
    hs = quan_li()
    ds.append(hs)

ds_trung = quan_li.trung_tuyen(ds)
ds_trung_tuyen_sap_xep = sorted(ds_trung, key=lambda ts: ts.tong_diem(), reverse=True) 

for thi_sinh in ds_trung_tuyen_sap_xep:
    thi_sinh.tra_thong_tin()