import pandas as pd
import numpy as np 
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1,5,[12]))

top_two = ser.value_counts().nlargest(2).index


ser = ser.where(ser.isin(top_two), other="other")

print("Series sau khi thay thế:")
print(ser)