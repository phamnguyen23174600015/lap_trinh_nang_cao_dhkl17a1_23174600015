import pandas as pd

myList = list("abcdefghijklmnopqrstuvwxyz") 
myArr = list(range(26))  

df = pd.DataFrame({
    'letters': myList,
    'numbers': myArr
})

print(df)