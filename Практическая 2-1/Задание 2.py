def data(candidates, target):
    resultat = []
    candidates.sort()
    def rekurs(combination, remained, start):
        if remained == 0:
            resultat.append(combination.copy())
            return
        if remained < 0:
            return
        for i in range(start,len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            combination.append(candidates[i])
            rekurs(combination, remained - candidates[i], i + 1)
            combination.pop()
    rekurs([],target, 0)
    return resultat
candidates = [10,1,2,7,6,1,5]
target = 8
result = data(candidates, target)
print(result)