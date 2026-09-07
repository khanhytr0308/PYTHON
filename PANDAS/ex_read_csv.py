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

#iloc
# print(df.iloc[0])

# print first rows
# print(df.iloc[0:1])

# take rows 4
# print(df.iloc[4:5])

#take first rows name
# print(df.iloc[0:1, 0:1])

#take rows 3 score
# print(df.iloc[3:4, 3:5])

# take the first 3 rows

# print(df.iloc[0:3])

#take all student but only Name and score

# print(df.iloc[: , [0, 3]])


#take the first 3 rows but only name age and score

# print(df.iloc[0:3, [0, 2, 3]])


