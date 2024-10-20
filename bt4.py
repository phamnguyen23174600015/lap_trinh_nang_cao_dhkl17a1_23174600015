import numpy as np

arr_zero = np.zeros(10)
arr_zero[4] = 1
print("arr zero: ",arr_zero)

arr_h = np.arange(10, 24)
arr_h_nguoc = arr_h[::-1]
print("arr h đảo ngược: ", arr_h_nguoc)

arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 1])
arr_1 = arr_k[arr_k != 0]  
print("arr_1 với các phần tử khác 0:", arr_1)

arr_1= np.append(arr_1, (10,20))
print("arr1 sau lhi thêm phàn tử: ", arr_1)

arr_1 = np.insert(arr_1 , 5, 100)
print("arr1 sau khi thay thế phần tử thứ 5 là: ", arr_1)

arr_1 = np.delete(arr_1, [0,1,2])
print("arr1 sau khi xóa các phần tử 0,1,2 là: ", arr_1)