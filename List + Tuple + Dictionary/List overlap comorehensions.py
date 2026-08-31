import random

a = random.sample(range(1,30), 12)
b = random.sample(range(1, 40), 11)

print(a)
print(b)


s = [i for i in a if i in b]

print(s)