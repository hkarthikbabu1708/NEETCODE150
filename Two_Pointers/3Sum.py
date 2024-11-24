# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
# and the indices i, j and k are all distinct.
#
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) -1

        while l < r:
            target = nums[i] + nums[l] + nums[r]

            if target == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1

            elif target < 0:
                l += 1
            else:
                r -= 1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))