num = int(input("number "))
check = int(input("number to check "))

if num % 2 == 0:
    print(f"{num} is even")
elif num % 4 == 0:
    print(num, "is a multiple of 4")
else:
    print(num, "is odd")

if num % check == 0:
    print(f"{num} chia het {check}")
else:
    print(f"{num} k chia het {check}")
