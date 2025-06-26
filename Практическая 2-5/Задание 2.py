def calculate(arr):
    positive = []
    for i in arr:
        if i > 0:
            positive.append(i)
    sum_pos = sum(positive)
    min_value = min(arr)
    min_index = arr.index(min_value)
    max_value = max(arr)
    max_index = arr.index(max_value)
    start = min(min_index, max_index)
    end = max(min_index, max_index)
    multiplication = 1
    for i in range(start, end + 1):
        multiplication *= arr[i]
    return sum_pos, multiplication
arr = [-2, -10, 2, 1, 7, 5]
result = calculate(arr)
print(f"Смма положительных: {result[0]}, Произведения диапазона: {result[1]}")