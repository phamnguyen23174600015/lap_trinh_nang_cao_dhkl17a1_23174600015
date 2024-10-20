import numpy as np
ar_true = np.full((3,3), True)
print("arr true: ", ar_true)

arr_ID = np.array([10, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_ID.reshape(3, 3)
arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]]  
print("Array sau khi đổi cột 1 và cột 3:\n", arr_2D)

arr_2D[[0, 1], :] = arr_2D[[1, 0], :]
print("Array sau khi đổi dòng 1 và dòng 2:\n", arr_2D)

arr_2D = arr_2D[::-1]
print("Array sau khi đảo ngược các dòng:\n", arr_2D)

arr_2D = arr_2D[:, ::-1]
print("Array sau khi đảo ngược các cột:\n", arr_2D)

arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("Array có giá trị NaN không?:", has_nan)

arr_2D_null[np.isnan(arr_2D_null)] = 0
print("Array sau khi thay thế NaN bằng 0:\n", arr_2D_null)