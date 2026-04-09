import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('../files/data.csv')

# print(df.to_string())
# df.loc[10,"Duration"] = 45
# print(df.to_string())

# print(df.index)

# for x in df.index:
#     if(df.loc[x,"Duration"]) > 300:
#         df.loc[x,"Duration"] = 300
# print(df.to_string())

# for x in df.index:
#     if(df.loc[x,"Duration"]) > 300:
#         df.drop(x,inplace=True)


# print(df.to_string())


# print(df.duplicated().to_string())

# df.drop_duplicates(inplace=True)
# print(df.duplicated().to_string())


# print(df.corr())


# df.plot()
# plt.show()


# df.plot(kind='scatter',x='Duration',y='Calories')
# plt.show()

# df.plot(kind='scatter',x='Duration',y='Maxpulse')
# plt.show()

df['Duration'].plot(kind='hist')
plt.show()