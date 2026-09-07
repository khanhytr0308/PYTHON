import pandas as pd

data = {
    "Score": [
        5,
        6,
        7,
        8,
        8,
        9,
        10
    ]
}

df = pd.DataFrame(data)

print(df.describe())