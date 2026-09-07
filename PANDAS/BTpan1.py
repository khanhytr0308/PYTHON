import pandas as pd

data = {
    "MSSV": ["SV001", "SV002", "SV003", "SV004", "SV005", "SV006", "SV007"],
    "Name": ["An", "Binh", "Cuong", "Dung", "Hung", "Nam", "Long"],
    "Age": [19, 20, 19, 21, 20, 19, 20],
    "Python": [8, 9, 6, 7, 10, 8, 7],
    "SQL": [7, 8, 9, 6, 9, 8, 7]
}

df = pd.DataFrame(data)
# print(df.head(3))
# print(df.tail(2))
print(df.info())
print(df.describe())

# have 5 rows
# have 5 columns
# row 3, 4, 5 are int
# row 1, 2 are str

# mean python is 7.857143 
# mean SQL is 7.714286
# max Python point is 10
# min SQL is 6
# in this class Python points are bester than SQL point