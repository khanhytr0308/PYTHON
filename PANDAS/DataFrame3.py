import pandas as pd

data = {
    "Name": ["An", "Binh", "Cuong"],
    "Python": [8, 9, 6],
    "SQL": [7, 8, 9]
}

df = pd.DataFrame(data)

print(df)