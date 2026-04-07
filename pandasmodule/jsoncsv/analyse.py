import pandas as pd

dt = pd.read_json("..//files/data.json")

# print(dt)
# print(dt.head(1))
# print(dt.head())

print(dt.tail())
print(dt.tail(1))
print(dt.info())

