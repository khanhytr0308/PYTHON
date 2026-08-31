import random

a = random.randint(1, 9)

#b = int(input("guess one"))
while True:
    b = int(input("guess one"))
    if b == a:
        print("exactly")
        break
    if b > a:
        print("high")
    if b < a:
        print("low")

    if input("Continue? Y/N: ") == 'N':
        break
    
