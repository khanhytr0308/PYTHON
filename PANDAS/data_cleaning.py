import pandas as pd

df = pd.read_csv("students_dirty.csv")


#inspect the data

print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())

#Analyze the missing data
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

df["Major"] = df["Major"].fillna("Unknown")

#find duplicate students

print(df.duplicated())
print(df[df.duplicated()])

df = df.drop_duplicates()

print(df.isnull().sum())
print(df.duplicated().sum())

df.to_csv("students_clean.csv", index=False)

#how many studentd are in the final dataset
print(len(df))
#What is the average score after cleaning? i dont know

# Find students with Score ≥ 8
print(df[df["Score"] >= 8])
print(df[df["Major"] == 'Information Systems'])
print(df[(df["Age"] >= 20) & (df["Score"] >= 8)])

