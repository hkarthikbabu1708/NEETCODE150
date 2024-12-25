# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
#
# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.
#
# Input: l1 = [1,2,3], l2 = [4,5,6]
#
# Output: [5,7,9]
#
# Explanation: 321 + 654 = 975.

def add_num(l1, l2):
    dummy =  Node()
    curr = dummy
    carry = 0

    while l1 or l2:
        x = l1.value if l1 else 0
        y = l2.value if l2 else 0
        total = x + y + carry

        carry = total // 10
        curr.next = Node(total%10)
        curr = curr.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    if carry > 0:
        curr.next = Node(carry)

    return dummy.next
