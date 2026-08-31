n = int(input())

max = None
min = None

for i in range(n):

    x = int(input())

    if max is None or x > max:
        max = x
    if min is None or x < min:
        min = x

print(max, "max")
print(min, "min")
