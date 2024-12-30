import pandas as pd

# Tạo Series chứa các chuỗi ngày tháng với các định dạng khác nhau
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

ser_datetime = pd.to_datetime(ser, errors='coerce')

# Hiển thị kết quả
print(ser_datetime)