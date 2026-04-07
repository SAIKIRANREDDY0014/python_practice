import pandas as pd

# print(pd.__version__)

# a1 = [1,4,5,7,8]
# print(a1)

# dt = pd.Series(a1)
# print(dt)
# print(dt[0])

# index = ["a","b","c","d","e"]
# dt =  pd.Series(a1,index)
# print(dt)
# print(dt["e"])


a2 = {"sai" : 110 , "giri" : 111 , "lokus" : 112}
print(a2)

dt1 = pd.Series(a2)
print(dt1)
print(dt1["sai"])

dt1 = pd.Series(a2,index = ["sai"])
print(dt1)
