import numpy as np

arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

arr_c = np.intersect1d(arr_a, arr_b)
print("Các phần tử xuất hiện ở cả arr_a và arr_b:", arr_c)

arr_d = np.setdiff1d(arr_a, arr_b)
print("Các phần tử chỉ xuất hiện ở arr_a:", arr_d)

# Bước 3: Định nghĩa arr_e và tạo arr_f chứa các phần tử từ 5 đến 10
arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]
print("Các phần tử từ 5 đến 10 của arr_e:", arr_f)
