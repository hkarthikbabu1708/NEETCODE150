# Top problems solved as listed in the below link
# https://www.linkedin.com/posts/ashishmisal_25-important-leetcode-problems-help-you-to-activity-7282613163508781057-VB-3/?utm_source=share&utm_medium=member_ios

import  heapq
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

# def two_sum(nums, target):
#     d = {}
#     for i,v in enumerate(nums):
#         if (target-v) in d:
#             return [d[target-v], i]
#         d[v] = i
#
# nums = [2,7,11,15]
# target = 9
# print(two_sum(nums, target))

# Reverse Linked List
# def rev_list(head):
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

# def rom_to_inte(s):
#     value = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000,
#     }
#     total = 0
#     prev = 0
#     for c in reversed(s):
#         curr_value = value[c]
#         if curr_value < prev:
#             total -= curr_value
#         else:
#             total += curr_value
#         prev = curr_value
#     return total
#
# s = "III"
# print(rom_to_inte(s))

# Valid Palindrome
# def is_pal(s):
#     left = 0
#     right = len(s) -1
#
#     while left < right:
#         if not s[left].isalnum():
#             left += 1
#             continue
#         if not s[right].isalnum():
#             right -= 1
#             continue
#
#         if s[left].lower() != s[right].lower():
#             return False
#         left += 1
#         right -= 1
#     return True
#
# s = "A man, a plan, a canal: Panama"
# print(is_pal(s))


# Reverse a String
# def rev_string(s):
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#
#     return s
#
# s = ["h", "e", "l", "l", "o"]
# print(rev_string(s))

# Single Number

# def single_num(nums):
#     total = 0
#     for n in nums:
#         total ^= n
#     return total
#
# nums = [2,2,1]
# print(single_num(nums))

# Intersection of Two Arrays
# def inter(set1,set2):
#     set1 = set(nums1)
#     set2 = set(nums2)
#     return list(set1&set2)
#
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# print(inter(nums1,nums2))

# Fizz Buzz
# def fizz_buzz(n):
#     res = []
#     for i in range(1, n+1):
#         if i%3 == 0 and i%5 == 0:
#             res.append("FizzBuzz")
#         elif i%3 == 0:
#             res.append("Fizz")
#         elif i%5 == 0:
#             res.append("Buzz")
#         else:
#             res.append(str(i))
#     return res
#
# n = 3
# print(fizz_buzz(n))

# To Lower Case
# def toLowerCase(s):
#     return s.lower()

# House Robber
# def hou_rob(nums):
#     n = len(nums)
#     if n == 0:
#         return 0
#     if n == 1:
#         return nums[0]
#
#     prev2 = 0
#     prev1 = 0
#
#     for n in nums:
#         curr = max(prev1, (prev2+n))
#         prev2 = prev1
#         prev1 = curr
#     return prev1
#
# nums = [1,2,3,1]
# print(hou_rob(nums))

# Add Two Numbers
# def add_twolists(list1, list2):
#     if not list1 or not list2:
#         return []
#
#     carry = 0
#     curr = dummy = Node()
#     while list1 or list2 or carry:
#         x = list1.val if list1 else 0
#         y = list2.val if list2 else 0
#         total = x + y + carry
#         curr.next = Node(total%10)
#         carry = total // 10
#         curr = curr.next
#
#         list1 = list1.next if list1
#         list2 = list2.next if list2
#
#     return dummy.next











