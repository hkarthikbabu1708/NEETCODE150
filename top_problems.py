# Top problems solved as listed in the below link
# https://www.linkedin.com/posts/rajatgajbhiye_never-skip-to-solve-these-dsa-questions-activity-7285144549348302849-Y0cN/?utm_source=share&utm_medium=member_ios

import  heapq
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

# Two Sum

# def two_sum(nums,target):
#     d = {}
#
#     for index, value in enumerate(nums):
#         if (target-value) in d:
#             return [d[target-value], index]
#         d[value] = index
#
# nums = [2,7,11,15]
# target = 9
# print(two_sum(nums,target))

# Best Time to Buy and Sell Stock

# def bestbuy(prices):
#     max_profit = 0
#     min_price = float('inf')
#
#     for price in prices:
#         min_price = min(min_price, price)
#         curr_profit = price - min_price
#         max_profit = max(max_profit, curr_profit)
#     return max_profit
#
# prices = [7,1,5,3,6,4]
# print(bestbuy(prices))

# Maximum Subarray

# def max_subarray(nums):
#     res = nums[0]
#     total = 0
#
#     for n in nums:
#         total += n
#         res = max(res, total)
#         if total < 0:
#             total = 0
#     return res
#
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray(nums))

# Container With Most Water

# def most_water(height):
#     left = 0
#     right = len(height) - 1
#     max_area = 0
#
#     while left < right:
#         curr_area = min(height[right], height[left]) * (right-left)
#         max_area = max(max_area, curr_area)
#
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     return max_area
#
# height = [1,8,6,2,5,4,8,3,7]
# print(most_water(height))

# Rotate Array
# def rotate_array(nums,k):
#     n = len(nums)
#     k = k % n
#
#     nums.reverse()
#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
#     return nums
#
# nums = [1,2,3,4,5,6,7]
# k = 3
# print(rotate_array(nums,k))

# Reverse String

# def rev_string(s):
#     l = 0
#     r = len(s) - 1
#
#     while l < r:
#         s[l], s[r] = s[r], s[l]
#         l += 1
#         r -= 1
#     return s
#
# s = ["h","e","l","l","o"]
# # print(s[::-1])
# print(rev_string(s))

# Valid Palindrome
# def ispal(s):
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         if not s[left].isalnum():
#             left += 1
#             continue
#         if not s[right].isalnum():
#             right =- 1
#             continue
#
#         if s[left].lower() != s[right].lower():
#             return False
#
#         left += 1
#         right -= 1
#
#     return True
#
# s = "A man, a plan, a canal: Panama"
# print(ispal(s))

# Longest Substring Without Repeating Characters

# def long_ss_dup(s):
#     start = 0
#     max_char = 0
#     char_set = set()
#
#     for end in range(len(s)):
#         while s[end] in char_set:
#             char_set.remove(s[start])
#             start += 1
#         char_set.add(s[end])
#         max_char = max(max_char, end-start+1)
#     return max_char
#
# s = "abcabcbb"
# print(long_ss_dup(s))

# Group Anagrams

# def anagram_grp(strs):
#     d = defaultdict(list)
#     for s in strs:
#         sorted_word = tuple(sorted(s))
#         d[sorted_word].append(s)
#     return  list(d.values())
#
# strs = ["eat","tea","tan","ate","nat","bat"]
# print(anagram_grp(strs))

# Longest Palindromic Substring
# def long_pal_ss(s):
#     res = ""
#     reslen = 0
#
#     for i in range(len(s)):
#         left = i
#         right = i
#         while left >=0 and right < len(s) and s[left] == s[right]:
#             if (right-left+1) > reslen:
#                 reslen = right-left+1
#                 res = s[left:right+1]
#             left -= 1
#             right += 1
#
#         left = i
#         right = i+1
#         while left >0 and right < len(s) and s[left] == s[right]:
#             if (right-left+1) > reslen:
#                 reslen = right-left+1
#                 res = s[left:right+1]
#             left -= 1
#             right += 1
#     return res
#
#
# s = "babad"
# print(long_pal_ss(s))

# Reverse Linked List
# def reverse_linkedlist(head):
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

# Merge Two Sorted Lists
# def merge_linkedlist(list1, list2):
#     dummy = Node(0)
#     curr = dummy
#
#     while list1 and list2:
#         if list1.val < list2.val:
#             curr.next = list1
#             list1 = list1.next
#         else:
#             curr.next = list2
#             list2 = list2.next
#         curr = curr.next
#
#     curr.next - list1 or list2
#
#     return dummy.next

# 1 2 3 4 5

# Remove Nth Node From End of List
# def remove_nthnode_linkedlist(head, n):
#     dummy = Node(0, head)
#     left = dummy
#     right = head
#
#     while n > 0:
#         right = right.next
#         n -= 1
#
#     while right:
#         right = right.next
#         left = left.next
#
#     left.next = left.next.next
#     return dummy.next

# Linked List Cycle
# def detect_cycle(head):
#     slow = fast = head
#
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#
#         if slow == fast:
#             return True
#     return False

# Intersection of Two Linked Lists
# def inter_linklists(headA, headB):
#     if not headA or not headB:
#         return None
#
#     one = headA
#     two = headB
#
#     while one != two:
#         one = two if one is None else one.next
#         two = one if two is None else two.next
#
#     return one

# Maximum Depth of Binary Tree

#recursive
# def max_depth(root):
#     if not root:
#         return 0
#
#     left = max_depth(root.left)
#     right = max_depth(root.right)
#
#     return 1 + max(left, right)

#iterative
# def max_depth(root):
#     if not root:
#         return 0
#
#     max_depth = 0
#     stack = [(root, 1)]
#
#     while stack:
#         node, depth = stack.pop()
#         max_depth = max(max_depth, depth)
#
#         if node.left:
#             stack.append((node.left, depth+1))
#         if node.right:
#             stack.append((node.right, depth+1))
#     return max_depth

# Validate Binary Search Tree
# def validate_bst(root):
#     def helper(root, low, high):
#         if not root:
#             return True
#
#         if not (low < root.val < high):
#             return False
#
#         return ((helper(root.left, low, root.val) and helper(root.right, root.val, high)))
#     return helper(root, float('-inf'), float('inf'))

# Symmetric Tree
# def sym_tree(root):
#     if not root:
#         return True
#
#     def helper(left, right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#
#         return left.val == right.val and
#                 helper(left.left, right.right) and
#                 helper(left.right, right.left)
#
#     return helper(root.left, root.right)

# Binary Tree Level Order Traversal
# def level_traversal(root):
#     if not root:
#         return []
#
#     queue = deque([root])
#     res = []
#
#     while queue:
#         curr_len = len(queue)
#         curr_level = []
#         for _ in range(curr_len):
#             node = queue.popleft()
#             curr_level.append(node.val)
#
#             if not node.left:
#                 queue.append(node.left)
#             if not node.right:
#                 queue.append(node.right)
#         res.append(curr_level)
#     return res

# Lowest Common Ancestor of a Binary Tree

# def lo_common_ancestor(root,p,q):
#     if not root or root == p or root == q:
#         return root
#
#     left = lo_common_ancestor(root.left, p, q)
#     right = lo_common_ancestor(root.right, p, q)
#
#     if left and right:
#         return root
#
#     return left if left else right

# Merge sort
# large datasets/stable sorting/extra space

# def merge(left, right):
#     i = j = 0
#     res = []
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res
#
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])
#
#     return merge(left, right)
#
# nums = [5,2,3,1]
# print(merge_sort(nums))

# Quick sort
# General purpose/fast in practice

# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     pivot = nums[-1]
#     left = [x for x in nums[:-1] if x < pivot]
#     right = [x for x in nums[:-1] if x > pivot]
#
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
# nums = [5,2,3,1]
# print(quick_sort(nums))

# Binary Search
# def binary_search(nums, target):
#     l = 0
#     r = len(nums) - 1
#
#     while l <= r:
#         mid = (l + r) // 2
#         if nums[mid] < target:
#             l = mid + 1
#         elif nums[mid] > target:
#             r = mid - 1
#         else:
#             return mid
#     return -1
#
# nums = [-1,0,3,5,9,12]
# target = 9
# print(binary_search(nums, target))

# Search in Rotated Sorted Array
# def rotated_bin(nums, target):
#     l = 0
#     r = len(nums) - 1
#
#     while l <= r:
#         mid = (l + r) // 2
#
#         if nums[mid] == target:
#             return mid
#
#         if nums[l] <= nums[mid]:
#             #leftside sorted
#             if nums[l] <= target < nums[mid]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         else:
#             #rightside sorted
#             if nums[mid] < target <= nums[r]:
#                 l = mid + 1
#             else:
#                 r = mid -1
#     return -1
#
# nums = [4,5,6,7,0,1,2]
# target = 0
# print(rotated_bin(nums, target))

#First Bad Version

# def is_ver(version):
#     return version >= 1
#
# def bad_ver(n):
#     l = 1
#     r = n
#
#     while l < r:
#         mid = (l + r) // 2
#         if is_ver(mid):
#             r = mid
#         else:
#             l = mid +1
#     return l
#
# n = 1
# print(bad_ver(n))





# Fibonacci Number
# Method 1 - Recursive

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     return fib(n-1) + fib(n-2)

# Method 2 - Dynamic programming
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#
#     return dp[n]

# Method 3 - Iterative

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     prev2 = 0
#     prev1 = 1
#
#     for i in range(2, n+1):
#         curr = prev1 + prev2
#         prev2 = prev1
#         prev1 = curr
#     return prev1
#
# n = 4
# print(fib(n))

# Climbing Stairs

# def climb_stairs(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     dp[2] = 2
#
#     for i in range(3,n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
#
# n = 3
# print(climb_stairs(n))

# Longest Increasing Subsequence
# def lis(nums):
#     res = []
#     for n in nums:
#         pos = bisect_left(res, n)
#         if pos == len(res):
#             res.append(n)
#         else:
#             res[pos] = n
#     return len(res)
#
# def lis(nums):
#     if not nums:
#         return 0
#     dp = [1] * len(nums)
#
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 dp[i] = max(dp[i], dp[j]+1)
#     return max(dp)
#
# nums = [10,9,2,5,3,7,101,18]
# print(lis(nums))

# Maximum Subarray
# def max_sub(nums):
#     res = nums[0]
#     total = 0
#
#     for n in nums:
#         total += n
#         res = max(res, total)
#         if total < 0:
#             total = 0
#     return res
#
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_sub(nums))

# Coin Change
# def coin_change(coins,amount):
#     if not coins:
#         return 0
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0
#
#     for amt in range(1, amount+1):
#         for coin in coins:
#             if amt >= coin:
#                 dp[amt] = min(dp[amt], dp[amt-coin] +1)
#     return dp[amount] if dp[amount] != float('inf') else -1
#
#
# coins = [1,2,5]
# amount = 11
# print(coin_change(coins,amount))


















