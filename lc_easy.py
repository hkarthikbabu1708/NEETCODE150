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






