arr = [-5, 3, 0, -9, 4]
for i in arr:
    if i > 0:
        print(i)
        break
for i in reversed(arr):
    if i < 0:
        print(i)
        break
firs_positiv = next(i for i in arr if i > 0)
last_negativ = next(i for i in reversed(arr) if i < 0)
print(firs_positiv, last_negativ)