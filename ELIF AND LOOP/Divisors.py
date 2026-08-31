num = int(input())

divisorList = []

for elem in range(1, num + 1):
    if(num % elem == 0):
        divisorList.append(elem)

print(divisorList)