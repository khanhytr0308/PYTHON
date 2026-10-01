import pandas as pd
import numpy as np

df = pd.read_csv("students_numpy_cleaning.csv")

print(df.isnull().sum())
print(df.shape)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Python"] = df["Python"].fillna(df["Python"].mean())
df["SQL"] = df["SQL"].fillna(df["SQL"].mean())
df["Major"] = df["Major"].fillna("no_name")

df = df.drop_duplicates()
print(df)
print(df[df.duplicated()])

