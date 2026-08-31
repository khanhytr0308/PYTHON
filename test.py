a = int(input())

count = 0
while a != 1:
  if a % 2 == 0:
    a = a // 2
    count += 1
  else:
    a = 3 * a + 1
    count += 1

print(f"{a} need {count} steps to 1")

