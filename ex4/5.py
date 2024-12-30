import pandas as pd
import numpy as np 
ser = pd.Series(np.random.normal(10,5,25))
print("Chuoi ser la:",ser)
#giá trị tối thiểuthiểu
gtri_toi_thieu = ser.min()
print("Gia tri toi thieu trong ser la:",gtri_toi_thieu)
#trung bình
median_ser = ser.median()
print("Trung vi cua ser la:",median_ser)
#phân vị
percentile_25 = ser.quantile(0.25)
print("Phan centile thu 25:",percentile_25)

percentile_75 = ser.quantile(0.75)
print("Phan centile thu 75:",percentile_75)

gtri_toi_da = ser.max()
print("Gia tri toi da cua ser:",gtri_toi_da)