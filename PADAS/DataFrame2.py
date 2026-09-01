import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [2000, 20, 50, 300],
    "Quantity": [5, 50, 30, 10]
}

df = pd.DataFrame(data)

print(df)