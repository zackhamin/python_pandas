import numpy as np
import pandas as pd
from numpy.random import randn

labels = ["a","b","c"]
my_data = [10,20,30]
arr = np.array(my_data)
d = {"a":10,"b":20,"c":30}

series_one = pd.Series(data = my_data)
print(series_one)

series_two = pd.Series(data = my_data, index=labels)
print(series_two)
#The data is the first arg, the index is the second

series_three = pd.Series(my_data,labels)
print(series_three)
#same as above but without the args labels

series_four = pd.Series(arr)
print(series_four)

series_five = pd.Series(d)
print(series_five)

ser1 = pd.Series([1,2,3,4],["USA","Germany","USSR","Japan"])
print(ser1)

ser2 = pd.Series([1,2,5,4], ["USA","Germany","Italy","Japan"])
print(ser2)

print(ser1["USA"])
#print out the label name to get the data value

print(ser1+ser2)
#adding them together will produce NaN for the indexes where the value does not match

#Dataframes
print("------------------------Data Frames-------------------------------------------------")
print(np.random.seed(101))

df = pd.DataFrame(randn(5,4),["A","B","C","D","E"],["W","X","Y","Z"])
print(df)