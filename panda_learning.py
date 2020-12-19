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
#Create a daya frame with random numbers, A - E are the Series, W - Z are the columns

print(df["W"])
#Select a column

print(df[["W","Z"]])
#Select a column

add_column = df["new"] = df["W"] + df["Y"]
#Add a new column
print(df)

df.drop("new", axis=1, inplace = True)
#To remove you need to refer inplace = true as otherwise Pandas will not remove it to save you accidentaly losing information. Then it is perma gone.
print(df)    

df.drop("E", axis=0, inplace = True)
print(df)
#Axis is preset to zero so you do not need to type it 


print(df.loc["A"])
#Print a row

print(df.iloc[2])
#Print a row using numerical value

print(df.loc["B","Y"])
#Select a specific row/column value

print(df.loc[["A","B"],["W","Y"]])