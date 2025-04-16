def array(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
nums = [1,2,3,1]
result = array(nums)
print(result)