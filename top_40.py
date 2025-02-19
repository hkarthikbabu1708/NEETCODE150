# https://www.linkedin.com/posts/rajatgajbhiye_dsa-on-sunday-here-are-40-most-asked-dsa-activity-7296752653588480000-wlbJ/?utm_source=share&utm_medium=member_ios&rcm=ACoAAAPSDI8BeKzF-mUYmODoQyoGYFc_GtvZ3yE

from collections import Counter, deque
import heapq


# Find the maximum sum subarray
# def max_sub(arr):
#     res = arr[0]
#     total = 0
#
#     for n in arr:
#         total += n
#         res = max(res, total)
#         if total < 0:
#             total = 0
#     return res
#
# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_sub(arr))

# Find all substrings that are palindromes
# def sub_pal(s):
#     out = []
#
#     for i in range(len(s)):
#         left = i
#         right = i
#
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             out.append(s[left:right + 1])
#             left -= 1
#             right += 1
#
#         left = i
#         right = i + 1
#
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             out.append(s[left:right + 1])
#             left -= 1
#             right += 1
#     return out
#
# s = "ababa"
# print(sub_pal(s))

# Implement the "Two Sum" problem
# def two_sum(nums,target):
#     d = dict()
#     for i,v in enumerate(nums):
#         if (target-v) in d:
#             return [d[target-v], i]
#         d[v] = i
#     return -1
#
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums,target))

# Find the Missing Number in an Array of Integers
# def miss_num(nums):
#     n = len(nums)
#     actual_sum = sum(nums)
#     expected_sum = ((n+1) * (n+2)) // 2
#     return expected_sum - actual_sum
#
# nums = [3, 7, 1, 2, 8, 4, 5]
# print(miss_num(nums))

# def mer_arr(arr1,arr2):
#     res = []
#     i = j = 0
#
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             res.append(arr1[i])
#             i += 1
#         else:
#             res.append(arr2[j])
#             j += 1
#
#     while i < len(arr1):
#         res.append(arr1[i])
#         i += 1
#
#     while j < len(arr2):
#         res.append(arr2[j])
#         j += 1
#
#     return res
#
# arr1 = [1, 3, 8]
# arr2 = [2, 4, 6, 7]
# print(mer_arr(arr1,arr2))

# Check if a string is a palindrome.
# def pal_str(s):
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         if not s[left].isalnum():
#             left += 1
#             continue
#
#         if not s[right].isalnum():
#             right -= 1
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
# print(pal_str(s))

# Find the first non-repeating character in a string.
# def non_rep(s):
#     # d = dict()
#     # for c in s:
#     #     d[c] = d.get(c, 0) + 1
#     # print(d)
#     count = Counter(s)
#     print(count)
#
#     for i,v in enumerate(s):
#         if count[v] == 1:
#             return i
#     return -1

# s = "leetcode"
# print(non_rep(s))

# Remove duplicates from a sorted array.
# def rem_dup(nums):
#     index = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i-1]:
#             nums[index] = nums[i]
#             index += 1
#     return len(nums[:index])
#
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# print(rem_dup(nums))

# Reverse a linked list
#1-2-3-4
# def rev_ll(head):
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

# Detect a cycle in a linked list.
# def detect_cycle(head):
#     slow = fast = head
#
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#
#         if slow == fast:
#             return True
#
#     return False

# Find the middle of a linked list
# 1 → 2 → 3 → 4
# def middle_ll(head):
#     slow = fast = head
#
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow

# # Merge two sorted linked lists
# def merge_ll(list1, list2):
#     dummy = Node()
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
#     if list1: curr.next = list1
#     if list2: curr.next = list2
#
#     return dummy.next

# Implement a stack using a linked list

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, value):
#         newnode = Node(value)
#         newnode.next = self.head
#         self.head = newnode
#
#     #1 - 2 -  3
#     def pop(self):
#         if self.is_empty():
#             return None
#         curr_value = self.head.value
#         self.head = self.head.next
#         return curr_value
#     def is_empty(self):
#         return self.head is None
#
#     def top(self):
#         if self.is_empty():
#             return None
#         return self.head.value

# Find the intersection point of two linked lists
# def inter_ll(list1, list2):
#     if not list1 or list2:
#         return None
#
#     one = list1
#     two = list2
#
#     while one != two:
#         one = one.next if one else list2
#         two = two.next if two else list1
#
#     return one










