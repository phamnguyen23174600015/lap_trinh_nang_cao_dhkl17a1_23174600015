import numpy as np
import pandas as pd

mylist = list("abcdefghijklmnopqrstuvwxyz")
myarr = np.arange(26)
myDict = dict(zip(mylist, myarr))

ser = pd.Series(myDict)
print(ser)