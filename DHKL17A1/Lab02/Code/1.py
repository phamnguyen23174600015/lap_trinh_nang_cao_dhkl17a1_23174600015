import numpy as np
#ngẫu nhiên nhiêtj độ
daily_temperatures = np.random.uniform(15, 35, 30)
print("nhiệt đôj ngẫu nhiên: ",daily_temperatures)
#làm tròn
daily_temperatures_rounded = np.round(daily_temperatures, 2)
print("nhiệt độ làm tròn: ",daily_temperatures_rounded)
#nhiệt độ tb và làm tròn
nhiet_do_tb = np.mean(daily_temperatures)
tb = np.round(nhiet_do_tb)

#nhiệt độ max và min
max = np.max(daily_temperatures)
min = np.min(daily_temperatures)

#ngày có nhiệt độ cao nhât và tháp nhất
day_max = np.argmax(daily_temperatures_rounded)  + 1 #argmax(min) trả về index của giá trị max(min)
day_min = np.argmin(daily_temperatures_rounded) + 1  #của dãy +1 vì bắt đầu dếm từ 0
print("ngày có nhiệt độ lớn nhấtnhất",day_max)
print("ngyaf có nhiệt độ thấp nhất",day_min)
#nhiệt độ chênh lệnh giẵ các ngày
temp_diff = [abs(daily_temperatures_rounded[i] - daily_temperatures_rounded[i-1]) for i in range(1, len(daily_temperatures_rounded))]
print("nhiệt độ chênh lệnh giữa các ngàyngày",temp_diff)
#ngày có nhiệt độ chênh lệch cao nhất
max_temp_diff = np.max(temp_diff)
day_max_temp_diff = np.argmax(temp_diff) + 1
print("ngày có nhiệt đọo tb cao nhất",day_max_temp_diff)

#ngày có nhiệt độ trên 20
temp_above20 = np.where(daily_temperatures_rounded > 20 )[0] + 1
temps_above_20 = daily_temperatures_rounded[daily_temperatures_rounded > 20]
print("ngày có nhiệt độ trên 20",temp_above20)
#đưa ra nhiệt độ của các ngày xác định
days = [5, 10, 15, 20]
temp_days = daily_temperatures_rounded[np.array(days)] - 1
print("nhiệt độ các ngày xcas định: ",temp_days)
#nhiệt độ các ngày trên trung bình
day_above_average = np.where(daily_temperatures_rounded > tb )[0] + 1
temp_above_average = daily_temperatures_rounded[daily_temperatures_rounded > 20]
print("nhiệt độ các ngày trên trung bình",temp_above_average)
#nhiệt độ các ngày chẵn lẻ
chan = np.arange(2, 31, 2)
le = np.arange(1, 31, 2)
temp_chan = daily_temperatures_rounded[chan - 1]
temp_le = daily_temperatures[le - 1]
print("nhiệt đô ngày chẵn",temp_chan)
print("nhiệt đọo ngày lẻ",temp_le)
