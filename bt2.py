import numpy as np
arr = np.arange(10)
print("loại dữ liệu: ", arr.dtype)
print("Kích thước dữ liệu: ", arr.size)
print("Các phần tử trong mảng: ", arr)
arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]
print("số lẻ: ", arr_odd)
print("Số chẵn: ", arr_even)
arr_1_update = np.where(arr % 2 == 0, arr,100 )
print("mảng đã được cập nhật: ", arr_1_update)