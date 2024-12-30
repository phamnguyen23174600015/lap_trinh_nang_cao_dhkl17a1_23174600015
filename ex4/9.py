import pandas as pd
import numpy as np 
ser = pd.Series(np.random.randint(1,10,35))
#np.random.randint(1, 10, 35): Tạo một mảng gồm 35 số nguyên ngẫu nhiên từ 1 đến 9 
#pd.series tạo một đối tượng series từ mảng vừa tạo

df = pd.DataFrame(ser.values.reshape(7, 5))

print("DataFrame có 7 hàng và 5 cột:",df)