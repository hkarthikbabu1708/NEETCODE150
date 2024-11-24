# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they
# add up to a given target number target
# and index1 < index2. Note that index1 and index2 cannot be equal,
# therefore you may not use the same element twice.

def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        new_target = numbers[l] + numbers[r]
        if new_target == target:
            return [l+1, r+1]
        elif new_target < target:
            l += 1
        else:
            r -= 1
    return []

numbers = [1,2,3,4]
target = 3
print(twoSum(numbers,target))