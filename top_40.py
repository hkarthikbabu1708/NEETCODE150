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

# Implement a stack using an array
# class stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.stack.pop()
#
#     def top(self):
#         if self.is_empty():
#             return None
#         return self.stack[-1]
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def size(self):
#         return len(self.stack)

# Implement a stack that supports push, pop, top, and retrieving the minimum element
# class stack:
#     def __init__(self):
#         self.stack = []
#         self.min = []
#
#     def push(self, value):
#         self.stack.append(value)
#         if not self.min or value <= self.min[-1]:
#             self.min.append(value)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         value =  self.stack.pop()
#         if value == self.min[-1]:
#             self.min.pop()
#         return value
#
#     def top(self):
#         if self.is_empty():
#             return None
#         return self.stack[-1]
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def size(self):
#         return len(self.stack)
#
#     def get_min(self):
#         if self.is_empty():
#             return None
#         return self.min[-1]

# Implement a circular queue
# class circularq:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.queue = [None] * capacity
#         self.front = 0
#         self.rear = 0
#         self.size = 0
#
#     def enqueue(self, value):
#         if self.size == self.capacity:
#             print("Queue is full!")
#             return
#         self.queue[self.rear] = value
#         self.rear = (self.rear + 1) % self.capacity  # Wrap around
#         self.size += 1
#
#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty!")
#             return None
#         value = self.queue[self.front]
#         self.queue[self.front] = None  # Optional: Clear the slot
#         self.front = (self.front + 1) % self.capacity  # Wrap around
#         self.size -= 1
#         return value
#
#     def front(self):
#         if self.is_empty():
#             print("Queue is empty!")
#             return None
#         return self.queue[self.front]
#
#     def is_empty(self):
#         return self.size == 0
#
#     def size(self):
#         return self.size()

# Design a max stack that supports push, pop, top, and retrieve the maximum element
# class stack:
#     def __init__(self):
#         self.stack = []
#         self.max = []
#
#     def push(self, value):
#         self.stack.append(value)
#         if not self.max or value >= self.max[-1]:
#             self.max.append(value)
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         value =  self.stack.pop()
#         if value == self.max[-1]:
#             self.max.pop()
#         return value
#
#     def top(self):
#         if self.is_empty():
#             return None
#         return self.stack[-1]
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def size(self):
#         return len(self.stack)
#
#     def get_max(self):
#         if self.is_empty():
#             return None
#         return self.max[-1]

# Design a queue using stacks
# class queue:
#     def __init__(self):
#         self.queue1 = []
#         self.queue2 = []
#
#     def enqueue(self, value):
#         self.queue1.append(value)
#
#     def dequeue(self):
#         if not self.queue2:
#             while self.queue1:
#                 self.queue2.append(self.queue1.pop())
#         return self.queue2.pop() if self.queue2 else None
#
#     def front(self):
#         if not self.queue2:
#             while self.queue1:
#                 self.queue2.append(self.queue1.pop())
#         return self.queue2[-1] if self.queue2 else None
#
#     def is_empty(self):
#         return len(self.queue1) == 0 and len(self.queue2) == 0
#
#     def size(self):
#         return len(self.queue1) + len(self.queue2)

# Find the Height of a Binary Tree
#Recursive
# def height_bt(root):
#     if not root:
#         return 0
#
#     return 1 + max(height_bt(root.left), height_bt(root.right))
# #Iterative
# def height_bt(root):
#     if not root:
#         return 0
#
#     stack = [(root, 1)]
#     max_depth = 0
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

# Find the Lowest Common Ancestor of Two Nodes in a Binary Tree
# def common_an(root,p, q):
#     if not root:
#         return None
#
#     if root.value == p.value or root.value == q.value:
#         return root
#
#     left = common_an(root.left, p, q)
#     right = common_an(root.right, p, q)
#
#     if left and right:
#         return root
#
#     return left if left else right

# Validate if a Binary Tree is a Valid Binary Search Tree
# def is_valid_bst(root):
#     def helper(node, low, high):
#         if not node:
#             return True
#         if not (low <= node.value < high):
#             return False
#         return (helper(node.left, low, node.value) and helper(node.right, node.value, high))
#     return helper(root, float('-inf'), float('inf'))

# Serialize and Deserialize a Binary Tree
# def ser_bt(root):
#     def dfs(root):
#         if not root:
#             return ["None"]
#         return [str(root.value)] + dfs(root.left) + dfs(root.right)
#     return ','.join(dfs(root))
#
# def deser_bt(data):
#     values = iter(data.split(","))
#     def dfs():
#         value = next(values)
#         if value == "None":
#             return None
#         root = TreeNode(int(value))
#         root.left = dfs()
#         root.right = dfs()
#         return root
#     return dfs()

# Implement an inorder traversal of a binary tree
#left - node - right

# def in_order(root):
#     res = []
#     def traverse(root):
#         if root:
#             traverse(root.left)
#             res.append(root.value)
#             traverse(root.right)
#     traverse(root)
#     return res

# Mirror Tree
# def mirror_tree(root):
#     if not root:
#         return None
#
#     left_tree = mirror_tree(root.left)
#     right_tree = mirror_tree(root.right)
#
#     root.left, root.right = right_tree, left_tree
#
#     return root

def diameter_bt(root):
    diameter = 0
    def height(node):
        nonlocal diameter
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        diameter = max(diameter, left_height+right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return diameter
























