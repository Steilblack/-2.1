C = 'a'
A = ["Aple", "aha", "banana","a", "aaa"]
count = 0
for i in A:
    if len(i) > 1 and i.startswith(C) and i.endswith(C):
        count += 1
        print(i, end=" ")
print()
print(count)

result = [i for i in A if len(i) > 1 and i.startswith(C) and i.endswith(C)]
coun = len(result)
print(result)
print(coun)

rezult = list(filter(lambda s: len(s) > 1 and s.startswith(C) and s.endswith(C), A))
cou = len(rezult)
print(rezult)
print(cou)