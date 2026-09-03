import pandas as pd

data = { 
    "Name": ["khanh", "khoa", "hai", "an", "le", "binh", "khang", "huy", "tai", "chuong"],
    "MSSV": ["b001", "b002", "b003", "b004", "b005", "b006", "b007", "b008", "b009", "b010"],
    "POINT": [10, 9, 8, 7, 6, 5, 6, 7, 8, 9]
}
df = pd.DataFrame(data)



print(df.tail(3))
print(df.head(3))
df.info()
print(df.describe())
print(df)