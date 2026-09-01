import pandas as pd

s = pd.Series(
    [8.5, 7.0, 9.0],
    index = ["An", "Binh", "Cuong"]
    )

print(s["An"])
print(s["Binh"])
print(s["Cuong"])
