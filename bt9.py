import csv

# Đọc dữ liệu từ file CSV
with open('euro2012.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# 1. In giá trị cột Goals
print("1. Giá trị cột Goals:")
for row in data:
    print(row['Goals'])

# 2. Số đội tham gia Euro2012
teams = {row['Team'] for row in data}  # Sử dụng set để loại bỏ trùng lặp
num_teams = len(teams)
print(f"\n2. Số đội tham gia Euro2012: {num_teams}")

# 3. In thông tin của Euro2012
print("\n3. Thông tin của Euro2012:")
print(f"Số dòng: {len(data)}, Số cột: {len(data[0])}")

# 4. Tạo dataframe mới chỉ chứa các cột 'Team', 'Yellow Cards', 'Red Cards'
discipline = [(row['Team'], row['Yellow Cards'], row['Red Cards']) for row in data]
print("\n4. Dataframe discipline:")
for entry in discipline:
    print(entry)

# 5. Sắp xếp discipline theo 'Red Cards', rồi 'Yellow Cards'
discipline_sorted = sorted(discipline, key=lambda x: (-int(x[2]), -int(x[1])))
print("\n5. Dataframe discipline đã sắp xếp:")
for entry in discipline_sorted:
    print(entry)

# 6a. Tính trung bình Yellow Cards
avg_yellow_cards = sum(int(row['Yellow Cards']) for row in data) / len(data)
print(f"\n6a. Trung bình Yellow Cards: {avg_yellow_cards:.2f}")

# 6b. Lọc các đội đã ghi hơn 6 bàn thắng
print("\n6b. Các đội đã ghi hơn 6 bàn thắng:")
for row in data:
    if int(row['Goals']) > 6:
        print(row['Team'])

# 7. In các đội mà tên bắt đầu bằng 'G'
print("\n7. Các đội có tên bắt đầu bằng 'G':")
for row in data:
    if row['Team'].startswith('G'):
        print(row['Team'])

# 8. In 7 cột đầu của euro12
print("\n8. 7 cột đầu của euro12:")
for row in data:
    print(list(row.values())[:7])

# 9. In tất cả các cột, trừ 3 cột cuối
print("\n9. Tất cả các cột, trừ 3 cột cuối:")
for row in data:
    print(list(row.values())[:-3])

# 10. In các cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards
print("\n10. Các cột được chỉ định:")
for row in data:
    print((row['Team'], row['Goals'], row['Shooting Accuracy'], row['Yellow Cards'], row['Red Cards']))

# 11. In các cột 'Team', 'Shooting Accuracy' cho England, Italy, Russia
print("\n11. Thông tin 'Team', 'Shooting Accuracy' cho England, Italy, Russia:")
for row in data:
    if row['Team'] in ['England', 'Italy', 'Russia']:
        print((row['Team'], row['Shooting Accuracy']))