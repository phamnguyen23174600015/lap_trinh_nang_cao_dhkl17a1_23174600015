import threading
import random

# Hàm để tìm giá trị lớn nhất trong một danh sách con
def tim_max_list_con(sub_list, ket_qua, index):
    ket_qua[index] = max(sub_list)

def main():
    # Tạo danh sách lớn với các phần tử ngẫu nhiên từ 0-100
    n = 100  # Số phần tử trong danh sách lớn
    so_thread = 5  # Số thread cần tạo
    danh_sach = [random.randint(0, 100) for _ in range(n)]

    # Chia danh sách lớn thành các danh sách con
    phan_kich_thuoc = n // so_thread
    danh_sach_con = [danh_sach[i * phan_kich_thuoc:(i + 1) * phan_kich_thuoc] for i in range(so_thread)]

    # Nếu danh sách lớn không chia hết cho số thread, thêm phần còn lại vào danh sách cuối
    if n % so_thread != 0:
        danh_sach_con[-1].extend(danh_sach[so_thread * phan_kich_thuoc:])

    # Mảng để lưu kết quả từ các thread
    ket_qua = [0] * so_thread

    # Tạo danh sách các thread
    threads = []
    for i in range(so_thread):
        thread = threading.Thread(target=tim_max_list_con, args=(danh_sach_con[i], ket_qua, i))
        threads.append(thread)
        thread.start()

    # Chờ tất cả các thread hoàn thành
    for thread in threads:
        thread.join()

    # Tìm giá trị lớn nhất cuối cùng từ các kết quả của thread
    max_cuoi_cung = max(ket_qua)

    # In kết quả
    print(f"Danh sách lớn: {danh_sach}")
    print(f"Kết quả từng thread: {ket_qua}")
    print(f"Giá trị lớn nhất: {max_cuoi_cung}")

if __name__ == "__main__":
    main()
