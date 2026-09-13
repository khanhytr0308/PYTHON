import pandas as pd

data = {
    "Name": ["Khanh", "Khoa", "Hai", "An", "Le"],
    "Age": [19, None, 20, None, 21],
    "Score": [8.5, 7.0, None, 9.0, None]
}

df = pd.DataFrame(data) 

df["Score"] = df["Score"].fillna(df["Score"].mean())

# df["Age"] = df["Age"].fillna(df["Age"]. mean())

df = df.dropna(subset=["Age"])

print(df)