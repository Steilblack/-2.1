import random
arr = []
for i in range(20):
    num = random.randint(0, 100)
    if num % 2 == 0:
        arr.append(num)
arr.sort()
print(arr)
