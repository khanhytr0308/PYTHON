import numpy as np

scores = np.array([
    [8, 7, 9],
    [6, 5, 7],
    [9, 10, 8],
    [4, 6, 5],
    [7, 8, 9]
])

print(np.mean(scores, axis =1))
print(np.mean(scores, axis=0))