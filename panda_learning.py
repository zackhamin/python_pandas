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

print(df.loc["G2"].loc[3]["B"])
#To grab a specific value in a cell

print(df.xs(1,level="Num"))
#Cross section which is easier than the loc method. The 1 represents the row we want the level represents the index name.

#MISSING DATA

d = {"A":[1,2,np.nan],"B":[5,np.nan,np.nan],"C":[1,2,3]}
print(d)

df = pd.DataFrame(d)
print(df)

print(df.dropna())
#prints any row without a null value in it. i.e if a row contains a null value the whole row is dropped

print(df.dropna(axis=1))
#prints any column without a null value in it. i.e. if a column contains a null value the whole column is dropped

print(df.dropna(thresh=2))
#Drop a row if it does not have atleast two values that are NOT NaN. So, two whole numbers.

print(df.fillna(value="Fill Value"))

fill_nan = df["A"].fillna(value=df["A"].mean())

print(fill_nan)

print("------------------------Group By-------------------------------------------------")

data = {"Company": [
    "GOOG","GOOG","MSFT","MSFT","FB","FB"],
    "PERSON":["SAM","CHARLIE","AMY","VANESSA","CARL","SARAH"],
    "SALES":[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)


byCompany = df.groupby("Company")
bySales = df.groupby("SALES")
print(byCompany.mean())
# To do analysis on a column you need to get the column name as a variable.
#Pandas will automatically get the column with integers and do the calculations

print(byCompany.sum())

print(byCompany.count())
# Returns the number of instances of a column, i.e. 2 people working at each company -
# 2 sets of sales values

print(bySales.max())
#highest value of sales per company

print(df.groupby("Company").sum().loc["FB"]) 
#One line method to return a specific value after being summed up.

print(df.groupby("Company").describe())
#Gives more detailed information on the total data. 

print("------------------------Merging Joining & Concatenating-------------------------------------------------")

#Concat is used to merge with the ability to merge on a key (column) or inner and outter.

print("------------------------Operations-------------------------------------------------")

df = pd.DataFrame({
    "col1": [1,2,3,4],
    "col2": [444,555,666,444],
    "col3": ["abc","def","ghi","xyz"]
})

print(df)

print(df["col2"].unique())
#Prints out an array of the unique values in column 2, no repeated values.

print(df["col2"].nunique())
#Prints out the length of the unique values array.

print(df["col2"].value_counts())
#Prints the values of the column with the number of times they appear.

print(df["col1"] > 2)
#Conditional operational method reminder True/False.

print(df[df["col1"] > 2])
#Conditional operational method reminder values.


def timesTwo(x):
    return x*2
#Custom function for below example

print(df["col1"].apply(timesTwo))
#Uses a custom function as a method. Returns values in col 1 X 2

print(df["col2"].apply(lambda x : x*2))
#Does the same as the above two methods but using a Lambda expression in one line


print(df["col3"].apply(len))
#Returns the length of each string value

sorted_column = df.sort_values("col2")
#Rearranges the rows based off of the values in column 1
print(sorted_column)

new_data = {
    "A":["foo","foo","foo","bar","bar","bar"],
    "B":["one","one","two","two","one","one"],
    "C":["x","y","x","y","x","y"],
    "D":[1,3,2,5,4,1]
}

new_data_frame = pd.DataFrame(new_data)

print(new_data_frame)

print(new_data_frame.pivot_table(values="D", index=["A","B"],columns=["C"]))
#Creates a pivot table, related to excel, which creates an index from A and B, Columns from values in C, which is x and y and values from D.
#So, foo two column Y returns NaN because in the original there is no foo with a Y value only an X value.
#Similarly bar two column X returns NaN because there is only a bar two with a value of Y

print("------------------------Data input and output-------------------------------------------------")

import_csv_and_read = pd.read_csv("../../Refactored_Py_DS_ML_Bootcamp-master/03-Python-for-Data-Analysis-Pandas/example")
print(import_csv_and_read)