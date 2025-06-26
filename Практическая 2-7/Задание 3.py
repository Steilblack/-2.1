number = [-1, -15, 0, 4, -4, 7, 20, 33, 100]
arr = []
for i in number:
    if i > 0 and i >= 10 and i <= 99:
        arr.append(i)
        print(i, end=" ")
print()
print(arr)