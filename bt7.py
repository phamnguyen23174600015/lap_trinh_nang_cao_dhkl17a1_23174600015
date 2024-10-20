import numpy as np

with open('baseball_2D.txt', 'r') as file:
    baseball = []
    for line in file:
        clean_line = line.replace('[', '').replace(']', '').replace(',', '')
        baseball.append(list(map(float, clean_line.strip().split())))


np_baseball = np.array(baseball)

print("Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
print("Kích thước của np_baseball:", np_baseball.shape)

print("Giá trị dòng thứ 50 trong np_baseball:", np_baseball[49, :])

np_weight = np_baseball[:, 1]
print("Array np_weight (cân nặng):", np_weight)

print("Chiều cao của vận động viên thứ 124:", np_baseball[123, 0])

mean_height = np.mean(np_baseball[:, 0])  
mean_weight = np.mean(np_baseball[:, 1])  
print("Chiều cao trung bình của các cầu thủ:", mean_height)
print("Cân nặng trung bình của các cầu thủ:", mean_weight)

correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
print("Hệ số tương quan giữa chiều cao và cân nặng:", correlation)
if correlation > 0:
    print("tương quan thuận")
elif correlation < 0:
    print("tương quan nghịch")
else:
    print("không có tương quan")
