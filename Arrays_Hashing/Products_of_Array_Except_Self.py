# Given an integer array nums, return an array output where output[i] is the
# product of all the elements of nums except nums[i].

def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    res = [0] * n

    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    for i in range(n):
        res[i] = left[i] * right[i]
    return res

# nums = [1,2,4,6]
nums = [-1,0,1,2,3]
print(productExceptSelf(nums))

