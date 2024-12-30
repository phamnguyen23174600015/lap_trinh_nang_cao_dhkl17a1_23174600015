import pandas as pd
import numpy as np 
ser = pd.Series(np.random.randint(1,10,7))
# Tìm vị trí của các số chia hết cho 3
positions = ser[ser % 3 == 0].index

print("Các số chia hết cho 3 trong ser nằm ở các vị trí:")
print(positions)