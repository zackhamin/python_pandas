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

# df.drop("E", axis=0, inplace = True)
# print(df)
#Axis is preset to zero so you do not need to type it 


print(df.loc["A"])
#Print a row

print(df.iloc[2])
#Print a row using numerical value

print(df.loc["B","Y"])
#Select a specific row/column value

print(df.loc[["A","B"],["W","Y"]])
#Obtain subsets

print("------------------------Data Frames Conditional Selection & Indexing-------------------------------------------------")

print(df> 0)
#Conditional selection operator returns true false

print(df)

booldf = df > 0
print(df[booldf])

print(df[df > 0])
# #Simplified version - returns NaN for false values

print(df["W"] > 0)

print(df[df["W"]>0])
# #Will print rows where column W is greater than zero

print(df[df["X"] < 0])
#Will print rows where column X is less than zero

print("---------------")
print(df[df["W"]<0]["Y"])
# Will print out the values in Column Y where the value of Row W is less than zero

print(df[df["W"]>0]["X"])
# Will print out the values in Column X where the value of Row W is more than zero

print("---------------")
print(df[(df["W"]>0) & (df["Y"]>1)])
# print a rows which meet multiple conditions set in the column. Python 'and' operator needs to be typed & because both conditions are true

newdf = df.reset_index()
print(newdf)
#Resets the Index from AB etc to 012 etc gives it a numerical index.

newind = "CA NY WY OR CO".split()

df["States"] = newind
print(df)
#Creates a new column States

set_index = df.set_index("States")
print(set_index)
#Sets states as the new index.

print(df)

print("------------------------Multi Index & Index Heirarchy-------------------------------------------------")

#Index levels
outside = ["G1","G1","G1","G2","G2","G2"]
inside = [1,2,3,1,2,3]

hier_index = list(zip(outside,inside))
#List of tuple pairs
print(hier_index)

hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,["A","B"])
#Multilevel index - Two sets of Indexes
print(df)

print(df.loc["G1"])
#print 1 set of data from first G1 set.

print(df.loc["G1"].loc[1])
#Print the data from line 1 in set 1 in a series

print(df.index.names)

df.index.names = ["Groups", "Num"]
print(df)