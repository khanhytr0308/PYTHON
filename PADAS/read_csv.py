import pandas as pd

df = pd.read_csv("students.csv")

# print(df)
# print(df["Name"])
# print(df[["Name", "Score"]])
# print(df[df["Score"] >= 8])
# print(df[df["Age"] == 19])

# print(df[(df["Score"] > 8) & (df["Age"] == 19)])

re = df[df["Score"] >= 8]

print(re["Name"])
