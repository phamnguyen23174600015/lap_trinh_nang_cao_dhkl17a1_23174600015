import pandas as pd
file_path = "Region.csv"  # Thay đường dẫn tới file CSV của bạn
df = pd.read_csv(file_path)

# In nội dung của file CSV
print(df)
