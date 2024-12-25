# You are given the beginning of a linked list head, and an integer n.
#
# Remove the nth node from the end of the list and return the beginning of the list.
#
# Example 1:
#
# Input: head = [1,2,3,4], n = 2
#
# Output: [1,2,4]

def remove_k_node(head, n):
    dummy = Node(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next
