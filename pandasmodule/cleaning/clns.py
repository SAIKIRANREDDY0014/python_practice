import pandas as pd

df = pd.read_csv('../files/data.csv')
# print(df.to_string())

# new_df = df.dropna()
# df.dropna(inplace= True)
# print(df.to_string())

# df.fillna(400.0,inplace=True)

# df.fillna({"Calories":444.4},inplace=True)
# print(df.to_string())


# print(df["Calories"].mean())
# print(df["Calories"].median())
# print(df["Calories"].mode()[0])

# wrong format data 

print(df["Duration"].to_string())
print(df["Duration"].dtype)
# pd.to_datetime(df["Duration"],format = 'mixed')

df["Duration"] = df["Duration"].str.strip()
df["Duration"] = df["Duration"].str.replace(r"\D", "", regex=True)
df["Duration"] = pd.to_numeric(df["Duration"],errors="coerce")
df.dropna(subset=['Duration'],inplace=True)
print(df["Duration"].to_string())
print(df["Duration"].dtype)

