import numpy as np
import pandas as pd

ser1 = pd.Series(list("abcdefghijklmnopqrstuvwxyz"))
ser2 = pd.Series(np.arange(26))

combined_df = pd.DataFrame({'letters': ser1, 'numbers': ser2})

print(combined_df)