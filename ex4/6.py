import pandas as pd
import numpy as np
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
# list('abcdefgh') tạo danh sách kí tự a đến h
# np.random.randint(8, size=30) tạo mảng 30 phần tử ngẫu nhiên từ 0 đến 7
# np.take(list('abcdefgh'), np.random.randint(8, size=30) lấy giá trị từ list('abcdefgh') theo chỉ số ngẫu nhiên
#pd.Series tạo đối tượng series từ mảng vừa tạo

value_counts = ser.value_counts()
print("Số lần xuất hiện của mỗi giá trị duy nhất trong ser là:",value_counts)