import numpy as np
import pandas as pd

labels = ["a","b","c"]
my_data = [10,20,30]
arr = np.array(my_data)
d = {"a":10,"b":20,"c":30}
print(arr)

series_one = pd.Series(data = my_data)
print(series_one)

series_two = pd.Series(data = my_data, index=labels)
series_three = pd.Series(my_data,labels)
print(series_two)
print(series_three)
