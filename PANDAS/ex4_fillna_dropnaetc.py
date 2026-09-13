import pandas as pd

data = {
    "Name": ["Khanh", "Khoa", "Hai", "An", "Khoa", "Le", "Hai"],
    "Age": [19, 20, None, 21, 20, None, 22],
    "Score": [8.5, None, 7.5, 9.0, None, 8.0, 7.5]
}

df = pd.DataFrame(data)
# check null data
# print(df.isnull().sum())

#fill none data by avg 
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Score"] = df["Score"].fillna(df["Score"].mean())

# check duplicated data
# print(df.duplicated())
print(df[df.duplicated()])

df = df.drop_duplicates(subset = ["Name"])

print(df)
