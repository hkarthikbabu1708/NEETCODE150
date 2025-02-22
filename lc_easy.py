# top interview questions leet code easy problems

# def two_sum(nums, target):
#     d = {}
#     for i,v in enumerate(nums):
#         if (target-v) in d:
#             return [d[target-v], i]
#         d[v] = i

# def roman_to_int(s):
#     roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     total = 0
#     prev_value = 0
#
#     for c in reversed(s):
#         curr_value = roman_values[c]
#         if curr_value >= prev_value:
#             total += curr_value
#         else:
#             total -= curr_value
#         prev_value = curr_value
#     return total
#
# s = "LVIII"
# print(roman_to_int(s))

# Longest Common Prefix
# def long_pfx(strs):
#     if not strs:
#         return ""
#     strs.sort()
#     first = strs[0]
#     second = strs[-1]
#
#     res = ""
#     for i in range(min(len(first), len(last))):
#         if first[i] != last[i]:
#             return res
#         res += first[i]
#
#     return res
#
# strs = ["flower", "flow", "flight"]
# print(long_pfx(strs))

# Valid Parentheses
# def is_valid(s):
#     brackets = {'(': ')', '{': '}', '[': ']'}
#     stack = []
#
#     for c in s:
#         if c in brackets:
#             stack.append(c)
#         else:
#             if not stack or c != brackets[stack.pop()]:
#                 return False
#     return len(stack) == 0
#
# s = "()[]{}"
# print(is_valid(s))

# Merge Two Sorted Lists
# def merge_two_lists(l1, l2):
#     dummy = Node(0)
#     curr = dummy
#
#     while l1 and l2:
#         if l1.value < l2.value:
#             curr.next = l1
#             l1 = l1.next
#         else:
#             curr.next = l2
#             l2 = l2.next
#         curr = curr.next
#
#     if l1: curr.next = l1
#     if l2: curr.next = l2
#
#     return dummy.next

# Remove Duplicates from Sorted Array
# def remove_duplicates(nums):
#     write_index = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i-1]:
#             nums[write_index] = nums[i]
#             write_index += 1
#     return write_index
#
# nums = [1, 1, 2]
# print(remove_duplicates(nums))

# Find the Index of the First Occurrence in a String
# def strStr(haystack, needle):
#     if not needle:
#         return 0
#
#     needle_length = len(needle)
#     for i in range(len(haystack) - needle_length + 1):
#         if haystack[i:i + needle_length] == needle:
#             return i
#
#     return -1
#
# haystack = "abc"
# needle = "c"
# # haystack = "hello"
# # needle = "ll"
# print(strStr(haystack,needle))

# Plus One
# def plus_one(digits):
#     for i in range(len(digits)-1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         else:
#             digits[i] = 0
#
#     return [1] + digits
#
# digits = [1,9,9]
# print(plus_one(digits))

# def climb_stairs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     dp = [0]  * (n + 1)
#     dp[1] = 1
#     dp[2] = 2
#
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
#
# n = 3
# print(climb_stairs(n))

# Merge Sorted Array
# def merge(nums1, nums2):
#     i = j = 0
#     res = []
#
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             res.append(nums1[i])
#             i += 1
#         else:
#             res.append(nums2[j])
#             j += 1
#
#     while i < len(nums1):
#         res.append(nums1[i])
#         i += 1
#
#     while j < len(nums2):
#         res.append(nums2[j])
#         j += 1
#
#     return res
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6,7, 8]
# print(merge(nums1, nums2))

# def merge(nums1,m, nums2,n):
#     i = m - 1
#     j = n - 1
#     k = len(nums1) - 1
#     print(i, j, k)
#
#     while i >= 0 and j >= 0:
#         if nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
#
#     # If there are remaining elements in nums2
#     while j >= 0:
#         nums1[k] = nums2[j]
#         j -= 1
#         k -= 1
#
#
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# print(merge(nums1, m, nums2, n))

# Binary Tree Inorder Traversal
#left root right
# def inorderTraversal(root):
#     res = []
#     def traverse(root):
#         if not root:
#             return None
#         traverse(root.left)
#         res.append(root.value)
#         traverse(root.right)
#     traverse(root)
#     return res

# Symmetric Tree
# def isSymmetric(root):
#     if not root:
#         return True
#
#     def helper(left, right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#
#         return ((left.val == right.val) and
#                 (helper(left.right, right.left)) and
#                 (helper(left.left, right.right)))
#
#     return helper(root.left, root.right)

# Convert Sorted Array to Binary Search Tree
# def sortedArrayToBST(nums):
#     mid = len(nums) // 2
#     root = Node(nums[mid])
#     root.left = sortedArrayToBST(nums[:mid])
#     root.right = sortedArrayToBST(nums[mid+1:])
#     return root

# def maxProfit(prices):
#     max_profit = 0
#     min_price = float('inf')
#
#     for p in prices:
#         min_price = min(min_price, p)
#         curr_profit = p - min_price
#         max_profit = max(curr_profit, max_profit)
#     return max_profit
#
# prices = [7, 1, 5, 3, 6, 4]
# print(maxProfit(prices))

# def getIntersectionNode(heada, headb):
#     if not heada or not headb:
#         return Null
#
#     one = heada
#     two = headb
#
#     while one != two:
#         one = one.next if one else headb
#         two = two.next if two else heada
#
#     return one

# Majority Element
# def maj_ele(nums):
#     d = {}
#     n = len(nums)
#
#     for num in nums:
#         d[num] = d.get(num, 0) + 1
#         if d[num] > n//2:
#             return num
#
# nums = [2,2,1,1,1,2,2]
# print(maj_ele(nums))

# Rotate Array
# def rot_arr(nums, k):
#     n = len(nums)
#     k = k % n
#     nums.reverse()
#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
#     return nums
#
# nums = [1,2,3,4,5,6,7]
# k = 3
# print(rot_arr(nums, k))

# def find_missing_ranges(nums, lower, upper):
#     res = []
#     print(nums)
#     nums = [lower - 1] + nums + [upper + 1]
#     print(nums)
#
#     for i in range(1, len(nums)):
#         if nums[i] - nums[i - 1] > 1:
#             # If the gap is more than 1, we have a missing range
#             start = nums[i - 1] + 1
#             end = nums[i] - 1
#             if start == end:
#                 res.append(str(start))  # Single number
#             else:
#                 res.append(f"{start}->{end}")  # Range
#     return res
#
# nums = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# print(find_missing_ranges(nums, lower, upper))

# def comb_sum(candidates, target):
#     def backtrack(start, target, path):
#         if target == 0:
#             res.append(path[:])
#             return
#         if target < 0:
#             return
#
#         for i in range(start, len(candidates)):
#             if candidates[i] > target:
#                 continue
#             path.append(candidates[i])
#             backtrack(i, target-candidates[i], path)
#             path.pop()
#
#     res = []
#     backtrack(0, target, [])
#     return res
#
# candidates = [2, 3, 6, 7]
# target = 7
# print(comb_sum(candidates, target))

# def prod_arr(nums):
#     n = len(nums)
#     res = [1] * (n)
#
#     left = 1
#     for i in range(n):
#         res[i] = left
#         left *= nums[i]
#
#     right = 1
#     for i in range(n-1, -1, -1):
#         res[i] *= right
#         right *= nums[i]
#     return res
#
# nums = [1, 2, 3, 4]
# print(prod_arr(nums))

# Reverse Bits
# def reverseBits(n):
#     res = 0
#     for i in range(32):
#         bit = n & 1
#         res = (res << 1) | bit
#         n >>= 1
#     return res
# n = 43261596
# print(reverseBits(n))

# Number of 1 Bits
# def hammingWeight(n):
#     count = 0
#     while n:
#         count += n & 1
#         n >>= 1
#     return count
#
# n = 11
# print(hammingWeight(n))

# def isHappy(n):
#     visited = set()
#     while n not in visited:
#         visited.add(n)
#         n = sumofsq(n)
#         if n == 1:
#             return True
#     return False
#
# def sumofsq(n):
#     output = 0
#     while n:
#         digit = n % 10
#         digit = digit**2
#         output += digit
#         n = n//10
#     return output
#
# n = 19
# print(isHappy(n))

# Reverse Linked List
# def reverseList(head):
#     curr = head
#     prev = None
#     next = None
#
#     while curr:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     return prev

# def strStr(haystack, needle):
#     if not needle:
#         return 0
#
#     for i in range(len(haystack) -len(needle)+1):
#         if haystack[i:i+len(needle)] == needle:
#             print(haystack[i:i+len(needle)])
#             return i
#
# haystack = "hello"
# needle = "ll"
# print(strStr(haystack, needle))

# Remove Element
# def removeElement(nums,val):
#     pos = 0
#     for i in range(len(nums)-1):
#         if nums[i] != val:
#             nums[pos] = nums[i]
#             pos += 1
#     return nums[:pos]
#
# nums = [3, 2, 2, 3]
# val = 3
# print(removeElement(nums, val))

from collections import Counter

# def intersect(nums1, nums2):
#     count1 = Counter(nums1)
#     count2 = Counter(nums2)
#     result = []
#     print(count1, count2)
#
#     for num in count1:
#         if num in count2:
#             result.extend([num] * min(count1[num], count2[num]))
#
#     return result
#
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# print(intersect(nums1, nums2))

# from collections import Counter
# def firstUniqChar(s):
#     count = Counter(s)
#     print(count)
#     d = {}
#     for c in s:
#         d[c] = d.get(c,0) + 1
#
#     for i,v in enumerate(s):
#         if d[v] == 1:
#             return i
#
#
# s = "leetcode"
# print(firstUniqChar(s))

# def fizzBuzz(n):
#     res = []
#     for i in range(1, n+1):
#         if i % 3 == 0:
#             res.append("Fizz")
#         elif i % 5 == 0:
#             res.append("Buzz")
#         elif i % 3 == 0 and i % 5 == 0:
#             res.append("FizzBuzz")
#         else:
#             res.append(str(i))
#     return res
#
# n = 5
# print(fizzBuzz(n))

# def pow(x,n):
#     return (x**n)
#
# x = 2.0
# n = 10
# print(pow(x,n))

# Move Zeroes

from collections import Counter
# def moveZeroes(nums):
#     index = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[index] = nums[i]
#             index += 1
#
#     for i in range(index, len(nums)):
#         nums[i] = 0
#     return nums
#
# nums = [0,1,0,3,12]
# print(moveZeroes(nums))