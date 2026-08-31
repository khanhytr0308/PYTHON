import numpy as np

a = np.arange(1,13)

print(a.shape)

b = a.reshape(3, 4)
print(b)
print(b[1:2, 0:3])
print(b[0:3, 3:4])
print(np.sum(b))