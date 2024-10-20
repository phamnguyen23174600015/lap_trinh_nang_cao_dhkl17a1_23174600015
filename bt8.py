import numpy as np

heights = [180, 182, 175, 177, 190, 185, 178, 180]
positions = ['GK', 'GK', 'M', 'M', 'D', 'D', 'A', 'A']

np_positions = np.array(positions, dtype='U5')
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

np_heights = np.array(heights, dtype='float')
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

gk_heights = np_heights[np_positions == 'GK']
mean_gk_height = np.mean(gk_heights)
print("Chiều cao trung bình của các GK:", mean_gk_height)

other_heights = np_heights[np_positions != 'GK']
mean_other_height = np.mean(other_heights)
print("Chiều cao trung bình của các vị trí khác:", mean_other_height)

players_dtype = np.dtype([('position', 'U5'), ('height', 'float')])
players = np.array(list(zip(np_positions, np_heights)), dtype=players_dtype)

players_sorted = np.sort(players, order='height')

tallest_player = players_sorted[-1]  
shortest_player = players_sorted[0]  

print("Cầu thủ cao nhất:", tallest_player['position'], "với chiều cao", tallest_player['height'])
print("Cầu thủ thấp nhất:", shortest_player['position'], "với chiều cao", shortest_player['height'])
