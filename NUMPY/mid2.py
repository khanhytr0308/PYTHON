import numpy as np

a = np.arange(1, 17).reshape(4, 4)

print(a)
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
print(np.mean(a, axis = 1))
print(np.max(a, axis = 1))