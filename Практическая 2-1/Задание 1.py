j = input("Введите драгоцености: ")
s = input("Введите камни: ")
count = 0
for i in s:
    if i in j:
        count += 1
print(count)
#Задание 3
def array(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
nums = [1,2,3,1]
result = array(nums)
print(result)