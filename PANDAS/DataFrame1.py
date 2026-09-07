import pandas as pd

data = {
    "ID": ["SV001", "SV002", "SV003", "SV004", "SV005"],
    "NAME": ["khanh", "khoa", "ha", "no", "yes"],
    "AGE": [18, 20, 21, 22, 23],
    "SCORE": [7.0, 7.2, 2.1, 1.2, 8.4]
}

df = pd.DataFrame(data)

print(df.tail(2))