import pandas as pd 

csvdata = pd.read_csv("C:/SAI KIRAN REDDY/BTECH/python/repo/python_practice/pandasmodule/files/csvcust.csv")
# print(csvdata)
# print(csvdata.to_string()) # use it to print entire dataframe
print(pd.options.display.max_rows) 
# pd.options.display.max_rows = 9999
# print(csvdata.loc[99])
# print(csvdata.loc[[99,98]])
