import pandas as pd
import numpy as np

# Tạo dữ liệu ngẫu nhiên
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

# In danh sách trọng lượng và loại quả
print(weights.tolist())  # In danh sách trọng lượng
print(fruit.tolist())  # In danh sách các loại quả

average_weights = weights.groupby(fruit).mean()

# Hiển thị kết quả
print("\nKhối lượng trung bình của từng loại quả:")
print(average_weights)