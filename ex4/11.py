import pandas as pd
import numpy as np 
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0,4,8,14,20]
# Trích xuất các phần tử tại các vị trí đã cho
result = ser.iloc[pos]

print(result)