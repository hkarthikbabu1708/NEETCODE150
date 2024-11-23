# Given an array of integers nums and an integer target, return the indices i and j such that
# nums[i] + nums[j] == target and i != j.

def twoSum(nums, target):
    d = dict()

    for i, v in enumerate(nums):
        complement = target - v
        if complement in d:
            return [d[complement], i]
        d[v] = i

# nums = [3, 4, 5, 6]
# target = 7
nums = [4,5,6]
target = 10
print(twoSum(nums,target))