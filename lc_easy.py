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

def getIntersectionNode(heada, headb):
    if not heada or not headb:
        return Null

    one = heada
    two = headb

    while one != two:
        one = one.next if one else headb
        two = two.next if two else heada

    return one
