x = int(input())

a = 0
b = 1

fi = []

for i in range(x):
    fi.append(a)

    a, b = b, a + b

print(fi)
