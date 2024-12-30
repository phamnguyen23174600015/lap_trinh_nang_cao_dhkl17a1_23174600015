import threading

def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)

def luong_giai_thua(n, ket_qua, chi_so):
    ket_qua[chi_so] = giai_thua(n)

if __name__ == "__main__":
    so = int(input("Nhập một số: "))
    ket_qua = [None] * so
    cac_luong = []

    for i in range(so):
        luong = threading.Thread(target=luong_giai_thua, args=(i + 1, ket_qua, i))
        cac_luong.append(luong)
        luong.start()

    for luong in cac_luong:
        luong.join()

    print(f"Giai thừa: {ket_qua}")