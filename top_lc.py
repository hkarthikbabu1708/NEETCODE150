# https://www.linkedin.com/posts/akashsinnghh_leetcode-problems-to-crack-your-next-coding-activity-7275172066625015810-rV88/?utm_source=share&utm_medium=member_ios

from collections import deque, Counter, defaultdict
import  heapq

# Linked List Cycle

# def is_cycle(list):
#     slow = fast = list
#
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#
#         if slow == fast:
#             return True
#     return False

# Removed duplicates from the sorted linked list

# def remove_dup(list):
#     curr = list
#
#     while curr and curr.next:
#         if curr.val == curr.next.val:
#             curr.next = curr.next.next
#         else:
#             curr = curr.next
#     return list

# add 2 numbers in linked list

# def add_ll(l1, l2):
#     dummy = Node(0)
#     curr = dummy
#     carry = 0
#
#     while l1 or l2 or carry:
#         x = l1.val if l1 else 0
#         y = l2.val if l2 else 0
#         total = x + y + carry
#         carry = total // 10
#         curr.next = Node(total%10)
#         curr = curr.next
#
#         if l1: l1 = l1.next
#         if l2: l2 = l2.next
#
#     return dummy.next

# Reverse Linked List

# 1 2 3 4 5
# def reverse_ll(list):
#     curr = list
#     prev = None
#     next = None
#
#     while curr:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#
#     return prev

# Valid Parenthesis

# def valid_par(s):
#     brackets = {'(' : ')', '{' : '}', '[' : ']'}
#     stack = []
#
#     for c in s:
#         if c in brackets:
#             stack.append(c)
#         else:
#             if not stack or brackets[stack.pop()] != c:
#                 return False
#     return len(stack) == 0
#
# s = "()[]{}"
# s = "(]"
# print(valid_par(s))

# Kth Largest Element in a Stream

# import heapq
# class kar:
#     def __init__(self, k, nums):
#         self.k = k
#         self.heap = []
#
#         for n in nums:
#             self.add(n)
#     def add(self, val):
#         heapq.heappush(self.heap, val)
#
#         if len(self.heap) > self.k:
#             heapq.heappop(self.heap)
#         return self.heap[0]

# from collections import Counter
# import heapq
# def k_frequent(nums, k):
#     count = Counter(nums)
#     heap = []
#
#     for value, freq in count.items():
#         heapq.heappush(heap, (-freq, value))
#
#     print(heap)
#     #     if len(heap) > k:
#     #         heapq.heappop(heap)
#     #
#     # return [ val for _,val in heap]
#
#     res = [heapq.heappop(heap)[1] for _ in range(k)]
#     return res

# nums = [1,1,1,2,2,3]
# k = 2
# print(k_frequent(nums, k))
#
# import heapq
# def k_pairs(nums1, nums2,k):
#     res = []
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             res.append((nums1[i], nums2[j]))
#     print(res)
#
#     heap = []
#     for val1, val2 in res:
#         total = val1 + val2
#         heapq.heappush(heap, (-total, (val1,val2)))
#
#         if len(heap) > k:
#             heapq.heappop(heap)
#     print(heap)
#
#     return [val for _, val in heap]
#
#
# nums1 = [1,7,11]
# nums2 = [2,4,6]
# k = 3
# print(k_pairs(nums1, nums2,k))

# def two_sum(nums, target):
#     d = {}
#     for i,v in enumerate(nums):
#         if (target-v) in d:
#             return [d[target-v], i]
#         d[v] = i
#
#
# # nums = [2,7,11,15]
# # target = 9
# nums = [3,2,4]
# target = 6
# print(two_sum(nums, target))

from collections import  defaultdict
# def group_anagram(strs):
#     d = dict()
#     for s in strs:
#         sorted_word = tuple(sorted(s))
#         if sorted_word in d:
#             d[sorted_word].append(s)
#         else:
#             d[sorted_word] = [s]
#     return list(d.values())

# from collections import defaultdict
#
# def group_anagram(strs):
#     anagram = defaultdict(list)
#     for word in strs:
#         sorted_word = tuple(sorted(word))
#         anagram[sorted_word].append(word)
#     return list(anagram.values())
#
# strs = ["eat","tea","tan","ate","nat","bat"]
# print(group_anagram(strs))

# def inter_two_arrays(nums1,nums2):
#     set1 = set(nums1)
#     set2 = set(nums2)
#     print(set1, set2)
#
#     return list(set1 & set2)
#
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# print(inter_two_arrays(nums1,nums2))

# def unique_emails(emails):
#     um = set()
#     for email in emails:
#         local, domain = email.split('@')
#         local = local.split('+')[0].replace('.', '')
#         unmail = local + '@' + domain
#         um.add(unmail)
#     print(um)
#     return len(um)
#
# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# print(unique_emails(emails))

# def un_char(s):
#     d = {}
#     for c in s:
#         d[c] = d.get(c,0) + 1
#     print(d)
#
#     for i, c in enumerate(s):
#         if d[c] == 1:
#             return i
#     return -1
#
# s = "leetcode"
# print(un_char(s))

# Number of Islands

# def no_island(grid):
#     no_of_island = 0
#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             if grid[row][col] == "1":
#                 dfs(grid, row, col)
#                 no_of_island += 1
#     return no_of_island
#
# def dfs(grid, row, col):
#     if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
#         return
#
#     grid[row][col] = "0"
#
#     dfs(grid, row - 1, col)
#     dfs(grid, row + 1, col)
#     dfs(grid, row, col - 1)
#     dfs(grid, row, col + 1)
#
#
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
#
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# print(no_island(grid))

# def max_area_island(grid):
#     max_area = 0
#
#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             if grid[row][col] == 1:
#                 curr_area = dfs(grid, row, col)
#                 max_area = max(max_area, curr_area)
#     return max_area
#
# def dfs(grid, row, col):
#     if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
#         return 0
#
#     grid[row][col] = 0
#     size = 1
#     size += dfs(grid, row - 1, col)
#     size += dfs(grid, row + 1, col)
#     size += dfs(grid, row, col - 1)
#     size += dfs(grid, row, col + 1)
#
#     return size
#
# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# print(max_area_island(grid))

# def undir_graph(n, edges):
#     graph = {i: [] for i in range(n)}
#     print(graph)
#
#     for edge in edges:
#         x , y = edge
#         graph[x].append(y)
#         graph[y].append(x)
#     print(graph)
#
#     def dfs(node, visited):
#         visited.add(node)
#         for child in graph[node]:
#             if child not in visited:
#                 dfs(child, visited)
#
#     visited = set()
#     count = 0
#
#     for node in range(n):
#         if node not in visited:
#             dfs(node, visited)
#             count += 1
#
#     return count
#
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
# print(undir_graph(n, edges))

# def word_ladder(beginWord, endWord, wordList):
#     if endWord not in wordList:
#         return 0
#
#     queue = deque([(beginWord, 1)])
#     visited = set()
#     visited.add(beginWord)
#
#     while queue:
#         word, length = queue.popleft()
#
#         for i in range(len(word)):
#             for c in "abcedefghijklmnopqrstuvwxyz":
#                 next_word = word[:i] + c + word[i+1:]
#
#                 if next_word == endWord:
#                     return length + 1
#
#                 if next_word not in visited and next_word in wordList:
#                     visited.add(next_word)
#                     queue.append((next_word, length+1))
#     return 0
#
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# print(word_ladder(beginWord, endWord, wordList))

# Maximum Depth of Binary Tree
# Iterative

# def max_depth_bt(root):
#     if not root:
#         return 0
#
#     stack = [(root, 1)]
#     max_depth = 0
#
#     while stack:
#         node, depth = stack.pop()
#         max_depth = max(max_depth, depth)
#         if node.left:
#             stack.append(node.right, depth+1)
#         if node.right:
#             stack.append(node.right, depth+1)
#     return max_depth

# Recursive

# def max_depth_bt(root):
#     if not root:
#         return 0
#
#     left_depth = max_depth_bt(node.left)
#     right_depth = max_depth_bt(node.right)
#
#     return 1 + max(left_depth, right_depth)

# def min_depth_bt(root):
#     if not root:
#         return 0
#
#     stack = [(root, 1)]
#     min_depth = float('inf')
#
#     while stack:
#         node, depth = stack.pop()
#         if not node.left and not node.right:
#             min_depth = min(min_depth, depth)
#         if node.left:
#             stack.append(node.left, depth+1)
#         if node.right:
#             stack.append(node.right, depth+1)
#     return min_depth

# def merge_bt(root1, root2):
#     if not root1 and not root2:
#         return None
#     if not root1:
#         return root2
#     if not root2:
#         return root1
#
#     root1.val += root2.val
#     root1.left = merge_bt(root1.left, root2.left)
#     root1.right = merge_bt(root1.right, root2.right)
#
#     return root1

# Convert Sorted Array to Binary Search Tree

# def convert_arr_to_bt(arr):
#     if not arr:
#         return None
#
#     mid = len(arr) // 2
#     root = Node(arr[mid])
#     root.left = convert_arr_to_bt(arr[:mid])
#     root.right = convert_arr_to_bt(arr[mid+1:])
#
#     return root

# def path_sum_bt(root, target):
#     if not root:
#         return False
#     stack = [(root, target-root.val)]
#
#     while stack:
#         node, rem  = stack.pop()
#         if not node.left and not node.right and rem == 0:
#             return True
#         if node.left:
#             stack.append(node.left, rem-node.left.val)
#         if node.right:
#             stack.append(node.right, rem-node.right.val)
#     return False


# def level_order(root):
#     if not root:
#         return []
#     res = []
#     queue = deque([root])
#
#     while queue:
#         length = len(queue)
#         curr_level = []
#
#         for i in range(length):
#             node = queue.popleft()
#             curr_level.append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         res.append(curr_level)
#     return res

# def zig_zag(root):
#     if not root:
#         return []
#
#     queue = deque([root])
#     left_to_right= True
#     res = []
#
#     while queue:
#         length = len(queue)
#         curr_level = []
#
#         for _ in range(length):
#             node = queue.popleft()
#
#             if left_to_right:
#                 curr_level.append(node.val)
#             else:
#                 curr_level.insert(0, node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         res.append(curr_level)
#         left_to_right = not left_to_right
#
#     return  res

# def valid_bt(root):
#     def helper(node, low, high):
#         if not node:
#             return True
#
#         if not (low < node.val < high):
#             return False
#
#         return helper(node.left, low, node.val) and helper(node.right, node.val, high)
#
#     return helper(root, float('-inf'), float('inf')

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[-1]
#     left_side = [x for x in arr[-1] if x <= pivot]
#     right_side = [x for x in arr[-1] if x > pivot]
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# def merge(left, right):
#     i = j = 0
#     res = []
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#
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
# nums = [5, 2, 3, 1]
# print(merge_sort(nums))

# def bubble_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     for i in range(len(nums) -1):
#         swapped = False
#         for j in range(len(nums)-i-1):
#             print(i, j)
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#                 swapped = True
#
#         if not swapped:
#             break
#     return nums
#
# nums = [5, 3, 8, 4, 2]
# print(bubble_sort(nums))

# def subset(nums):
#     res = []
#     def backtrack(start, path):
#         res.append(path[:])
#
#         for i in range(start, len(nums)):
#             path.append(nums[i])
#             backtrack(i+1, path)
#             path.pop()
#     backtrack(0, [])
#     return res
#
# nums = [1,2,3]
# print(subset(nums))

# def subset_dup(nums):
#
#     def backtrack(start, path):
#         res.append(path[:])
#         for i in range(start, len(nums)):
#             if start > 0 and nums[i] == nums[i-1]:
#                 continue
#             path.append(nums[i])
#             backtrack(i+1, path)
#             path.pop()
#     res = []
#     nums.sort()
#     backtrack(0, [])
#     return res
#
# nums = [1,2,1]
# print(subset_dup(nums))
#
# def permuations(nums):
#
#     def backtrack(path, used):
#         if len(nums) == len(path):
#             res.append(path[:])
#         for i in range(len(nums)):
#             if used[i]:
#                 continue
#             path.append(nums[i])
#             used[i] = True
#             backtrack(path, used)
#             path.pop()
#             used[i] = False
#
#     res = []
#     used = [False] * len(nums)
#     backtrack([], used)
#     return res
#
# nums = [1,2,3]
# print(permuations(nums))

# def combination_sum(candidates, target):
#     def backtrack(start, target, path):
#         if target == 0:
#             res.append(path[:])
#             return res
#
#         if target < 0:
#             return
#
#         for i in range(start, len(candidates)):
#             path.append(candidates[i])
#             backtrack(i, target-candidates[i], path)
#             path.pop()
#
#     res = []
#     backtrack(0, target, [])
#     return res
#
# candidates = [2,3,6,7]
# target = 7
# print(combination_sum(candidates, target))

# def long_ss(s):
#     count = 0
#     char_set = set()
#     start = 0
#
#     for end in range(len(s)):
#         while s[end] in char_set:
#             char_set.remove(s[start])
#             start += 1
#         char_set.add(s[end])
#         count = max(count, end-start+1)
#     return count
#
# s = "abcabcbb"
# print(long_ss(s))

# def min_size_sub_array_sum(nums, target):
#     min_length = float('inf')
#     start = 0
#     total = 0
#
#     for end in range(len(nums)):
#         total += nums[end]
#
#         while total >= target:
#             min_length  = min(min_length, end-start+1)
#             total -= nums[start]
#             start += 1
#     return  min_length if min_length != float('inf') else 0
#
# nums = [2,3,1,2,4,3]
# target = 7
# print(min_size_sub_array_sum(nums, target))

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