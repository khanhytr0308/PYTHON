import pandas as pd

data = {
    "Name": ["Khanh", "Khoa", "Hai", "An", "Khoa", "Le", "Hai", "Minh"],
    "Age": [19, None, 20, 21, 20, None, 22, None],
    "Score": [8.5, 7.0, None, 9.0, 7.0, 8.0, None, 9.5]
}

df = pd.DataFrame(data)
# check none data
print(df.isnull().sum())

# fill none data by avg
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

# check dupliacated data
print(df.duplicated().sum())
print(df[df.duplicated()])

#delete duplicated data
df = df.drop_duplicates()

print(df)

# Check again
print(df.isnull().sum())
print(df.duplicated().sum())