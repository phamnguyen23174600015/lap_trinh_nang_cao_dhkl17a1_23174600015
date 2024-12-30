import pandas as pd
import numpy as np

# Tạo Series emails
emails = pd.Series(['buying books at amazom,com', 'ranese@egypt.com', 'matt@t.co', 'narendra@modi.com'])

# Biểu thức chính quy kiểm tra tính hợp lệ của email
pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

# Kiểm tra tính hợp lệ của các email
valid_emails = emails[emails.str.match(pattern)]

# Hiển thị kết quả
print(valid_emails)