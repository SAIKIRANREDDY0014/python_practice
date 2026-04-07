import pandas as pd

data = {
    "calories" : [420,380,289],
    "duration" : [50,34,67]
}

print(data)

dt = pd.DataFrame(data,index=["a","b","c"])
print(dt)
print(dt.loc["c"]) #return row
print(dt.loc[["a","c"]])  #return rows 