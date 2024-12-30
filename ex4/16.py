import pandas as pd

ser = pd.Series([1,3,6,10,15,21,27,35])

difference = ser.diff()

print(difference)