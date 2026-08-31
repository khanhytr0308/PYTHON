import numpy as np

image = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#print(image + 20)
#print(image - 10)
print(image[::-1])
print(image[1:3, 1:3])
print(np.max(image))