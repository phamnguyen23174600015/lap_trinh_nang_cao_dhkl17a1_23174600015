import pandas as pd
import numpy as np 

truth = pd.Series([10,9,6,5,3,1,12,8,13])
pred = pd.Series(range(10)) + np.random.random(10)

mse = ((truth - pred) ** 2).mean()

# Hiển thị kết quả
print(f"Sai số bình phương trung bình (MSE): {mse}")