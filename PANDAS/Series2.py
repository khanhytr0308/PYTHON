import pandas as pd

s = pd.Series(
    [8.5, 7.0, 9.0, 6.5, 8.0],
    index = ["SV001",'SV002', "SV003", "SV004", "SV005"]
    )

print(s)
print(s["SV001"])