import pandas as pd
import numpy as np 
ser = pd.Series(np.random.random(20))
# Chia dữ liệu thành 10 phần vị bằng nhau và gán nhãn phần vị
ser = pd.qcut(ser, q=10, labels=[f"Quantile {i}" for i in range(1, 11)])

print("Chuỗi dữ liệu sau khi thay thế bằng tên phần vị:")
print(ser)