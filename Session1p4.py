def non_decreasing(nums):
    count = 0
    for i in range(len(nums)-1):  # avoid index out of range
        if nums[i + 1] < nums[i]:   # fix: check for decreasing
            count += 1
            if count > 1:
                return False
    return True



     
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))