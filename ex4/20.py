import pandas as pd
import numpy as np
# Đọc file CSV
file = 'euro2012.csv'  
data = pd.read_csv(file)

# In giá trị của cột Goals
print("In giá trị cột Goals:")
print(data[['Team', 'Goals']])

#In số đội tham gia Euro2012
teams = data[['Team']]
print("Số đội tham gia Euro2012:")
print(teams)

#In thông tin Euro2012
print("In thông tin Euro 2012:",data)

#Tạo 1 data frame mới từ euro2012 có tên là discipline chỉ chứa 3 cột 'Team','Yellow Cards','Red Cards'
discipline = data[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# Sắp xếp giảm dần theo 'Red Cards' và sau đó theo 'Yellow Cards'
discipline_gdan = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])
print(discipline_gdan)

#Tính trung bình yellow cards
yellow_cards = data['Yellow Cards']
print("Trung bình Yellow Cards:",np.mean(yellow_cards))

# Lọc các đội ghi hơn 6 bàn thắng
goals_6 = data[data['Goals'] > 6]

# Hiển thị các đội ghi hơn 6 bàn thắng
print("Các đội ghi hơn 6 bàn thắng:")
print(goals_6[['Team', 'Goals']])

# Lọc các đội có tên bắt đầu bằng chữ 'G'
teams_g = data[data['Team'].str.startswith('G')]
print("Các đội có tên bắt đầu bằng chữ 'G':")
print(teams_g[['Team']])

#In 7 cột đầu của euro2012
# Hiển thị 7 cột đầu tiên của DataFrame
print("7 cột đầu của euro2012:")
print(data.iloc[:, :7])

# Hiển thị tất cả các cột trừ 3 cột ở cuối
print("Tất cả các cột trừ 3 cột ở cuối:")
print(data.iloc[:, :-3])

#In các cột Team, Goals,Shooting Accuracy, Yellow Cards,Red Cards
teams = data['Team']
goals = data['Goals']
shooting_accurary = data['Shooting Accuracy']
yellow_cards = data['Yellow Cards']
red_cards = data['Red Cards']
print("In cột Teams:",teams)
print("In cột Goals:",goals)

print("In cột shooting accuray",shooting_accurary)
print("In cột Yellow Cards:",yellow_cards)

print("In cột Red Cards:" ,red_cards)

#In các cột chỉ hiển thị 'Team','Shooting Accurary' từ 'England','Italy','Russia'
filtered_teams = data[data['Team'].isin(['England', 'Italy', 'Russia'])]
result = filtered_teams[['Team', 'Shooting Accuracy']]

print(result)