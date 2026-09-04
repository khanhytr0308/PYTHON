import pandas as pd

df = pd.read_csv("students.csv")


# condition
# s = df[df["Score"] < 7]

# print colums name
# print(s["Name"])

# print colums name and score
# r = df[df["Score"] >= 8]
# print(r[["Name", "Score"]])

#and codition
# re = df[(df["Score"] >= 8) & (df["Age"] == 19)]
# print(re["Name"])

# or codition
# print(df[(df["Score"] >= 8) | (df["Age"] == 20)])

#loc
# print(df.loc[df["Score"] >= 8, ["Name", "Score"]])
# print(df.loc[(df["Age"] == 19) & (df["Score"] >= 8)], ["Name", "Age", "Score"])

print(df.iloc[0])
