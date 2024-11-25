# You are given a non-empty array of integers nums. Every integer appears twice except for one.
# Return the integer that appears only once.

def singleNumber(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res

nums = [3,2,3]
print(singleNumber(nums))
