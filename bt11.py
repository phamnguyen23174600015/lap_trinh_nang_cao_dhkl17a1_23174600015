import json
from datetime import datetime

def luu_giao_dich(du_lieu_giao_dich, duong_dan_file):
    try:
        with open(duong_dan_file, 'r', encoding='utf-8') as f:
            du_lieu = json.load(f)
    except FileNotFoundError:
        du_lieu = []
    du_lieu.append(du_lieu_giao_dich)
    with open(duong_dan_file, 'w', encoding='utf-8') as f:
        json.dump(du_lieu, f, ensure_ascii=False, indent=4)


def ghi_giao_dich():
    loai_giao_dich = input("Nhập loại giao dịch: ")
    so_tien = float(input("Nhập số tiền giao dịch: "))
    thoi_gian_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"loai": loai_giao_dich,
            "so_tien": so_tien,
            "thoi_gian": thoi_gian_hien_tai}


file_giao_dich = 'nam-thang-nay-gio-phut-giay.json'  
while True:
    giao_dich = ghi_giao_dich()
    luu_giao_dich(giao_dich, file_giao_dich)
    tiep_tuc = input("tiếp tục ghi giao dịch? (1: Có, 0: Không): ")
    if tiep_tuc == '0':
        break

