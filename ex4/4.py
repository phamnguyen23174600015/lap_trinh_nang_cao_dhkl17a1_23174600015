import pandas as pd
import numpy as np 
ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([4,5,6,7,8])

result = ser1[~ser1.isin(ser2)]
result

symmetric_diff = pd.Series(np.setxor1d(ser1, ser2))
symmetric_diff