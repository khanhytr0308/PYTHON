# create array 1 2 3
#              4 5 6
#              7 8 9 
# print 5
# print colums 2
# print 2 3
#       5 6

import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[1, 1])
print(a[0:3, 1:2])
print(a[0:2, 1:3])