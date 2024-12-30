import pandas as pd

ser = pd.Series(['how','to','kick','ass?'])

ser_capitalized = ser.str.capitalize()

# Hiển thị kết quả
print(ser_capitalized)