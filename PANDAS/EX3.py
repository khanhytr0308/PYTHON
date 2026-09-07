import pandas as pd

data = {
    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Headphone",
        "Webcam"
    ],
    
    "Price": [
        2000,
        20,
        50,
        300,
        100,
        80
    ],
    
    "Quantity": [
        5,
        50,
        30,
        10,
        20,
        15
    ]
}

df = pd.DataFrame(data)

# print(df.tail(3))
# print(df.head(3))
print(df.info())
print(df.describe())

# laptop is most expensive
# mean cost is 425
# mean Quantity is 21.666667
# most expensive is 2000
# lowest price is 20
