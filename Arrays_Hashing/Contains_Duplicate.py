# Given an integer array nums, return true if any value appears more than once
# in the array, otherwise return false.

def hasDuplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False

# nums = [1, 2, 3, 3]
nums = [1, 2, 3, 4]
print(hasDuplicate(nums))