# You are given an array of integers nums containing n + 1 integers.
# Each integer in nums is in the range [1, n] inclusive.
#
# Every integer appears exactly once, except for one integer which appears two or more times.
# Return the integer that appears more than once.
# Input: nums = [1,2,3,2,2]
#
# Output: 2


def dupl_num(nums):
    d = set()
    for n in nums:
        if n in d:
            return n
        d.add(n)
    return -1

nums = [1, 2, 3, 2, 2]
print(dupl_num(nums))
