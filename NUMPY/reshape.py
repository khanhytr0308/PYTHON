import numpy as np

a = np.arange(12)

b = a.reshape(3, 4)
c = a.reshape(4, 3)
d = a.reshape(2, 6)
e = a.reshape(6, 2)
rell = a.reshape(-1, 2)

print(b)
print(c)
print(d)
print(e)
print(rell)

