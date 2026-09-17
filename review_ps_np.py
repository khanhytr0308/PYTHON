import pandas as pd
import numpy as np

df = pd.read_csv("students_numpy_cleaning.csv")

print(df.isnull().sum())
print(df.shape)

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)


