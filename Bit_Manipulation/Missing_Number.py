# Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

def missingNumber(nums):
    n = len(nums)
    curr_sum = sum(nums)
    act_sum = n * (n+1) // 2
    return act_sum - curr_sum

# nums = [1,2,3]
nums = [0,2]
print(missingNumber(nums))