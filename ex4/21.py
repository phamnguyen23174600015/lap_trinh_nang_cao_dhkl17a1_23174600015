import pandas as pd
import numpy as np
# Đọc dữ liệu từ tập tin drinks.csv với cột đầu tiên làm index
file = 'drinks.csv'
drink = pd.read_csv(file, index_col=0)

# In kiểu dữ liệu của biến 'drink'
print("Kiểu dữ liệu:", type(drink))

# In kích thước (số dòng và số cột) của dữ liệu
print("Kích thước:", drink.shape)

# Hiển thị tên các cột
print("Tên các cột:", drink.columns)

# Hiển thị 5 dòng dữ liệu đầu tiên
print("\n5 dòng dữ liệu đầu tiên:\n", drink.head())

# Hiển thị 5 dòng dữ liệu cuối cùng
print("\n5 dòng dữ liệu cuối cùng:\n", drink.tail())
# Nhóm theo châu lục và tính giá trị trung bình của số lượng bia tiêu thụ
average_beer_by_continent = drink.groupby('continent')['beer_servings'].mean()
print(average_beer_by_continent)

# Nhóm theo châu lục và tính thống kê mô tả cho số lượng rượu vang tiêu thụ
wine_stats_by_continent = drink.groupby('continent')['wine_servings'].describe()
print(wine_stats_by_continent)

#cho biết số lượng các loại bia và rượu tiêu thụ trung bình ở mỗi châu lục 
average_consumption_by_continent = drink.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].mean()
print(average_consumption_by_continent)

#cho biết giá trị trung vị(mean) cho các loại rượu tiêu thụ ở mỗi châu
mean_consumption_by_continent = drink.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].mean()
print(mean_consumption_by_continent)
#cho biết số lượng rượu mạnh tiêu thụ trung bình , lớn nhất nhỏ nhất ở mỗi châu lục
spirit_servings_tb = drink.groupby('continent')['spirit_servings'].mean()
spirit_servings_max = drink.groupby('continent')['spirit_servings'].max()
spirit_servings_min = drink.groupby('continent')['spirit_servings'].min()
print("Số lượng spirit_servings tiêu thụ trung bình:",spirit_servings_tb)
print("Số lượng spirit_servings tiêu thụ lớn nhất:",spirit_servings_max)
print("Số lượng spirit_servings tiêu thụ nhỏ nhất:",spirit_servings_min)


#sắp xếp tăng dần theo số liệu bia tiêu thụ 
#cho biết 5 quốc gia có lượng tiêu thụ bia nhiều nhất và ít nhất 
sorted_beer_data = drink[['country', 'beer_servings']].sort_values(by='beer_servings', ascending=True)
beer_min = sorted_beer_data.head(5)  # 5 quốc gia có ít bia tiêu thụ nhất
beer_max = sorted_beer_data.tail(5)  # 5 quốc gia có nhiều bia tiêu thụ nhất
print("\n5 quốc gia có lượng bia tiêu thụ ít nhất: \n", beer_min)
print("\n5 quốc gia có lượng bia tiêu thụ nhiều nhất: \n", beer_max)