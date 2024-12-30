import pandas as pd

ser1  = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df_doc = pd.concat([ser1, ser2], axis=0, ignore_index=True)

print("Xếp chồng theo chiều dọc:",df_doc)