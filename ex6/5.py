import threading
import requests

def lay_du_lieu(url):
    try:
        phan_hoi = requests.get(url)
        print(f"URL: {url} | Mã trạng thái: {phan_hoi.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"URL: {url} | Lỗi: {e}")

danh_sach_url = [
    "https://www.google.com",
]

cac_luong = []
for url in danh_sach_url:
    luong = threading.Thread(target=lay_du_lieu, args=(url,))
    cac_luong.append(luong)
    luong.start()

for luong in cac_luong:
    luong.join()