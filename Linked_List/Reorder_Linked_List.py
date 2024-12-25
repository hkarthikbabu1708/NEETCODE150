# You are given the head of a singly linked-list.
#
# The positions of a linked list of length = 7 for example, can intially be represented as:
#
# [0, 1, 2, 3, 4, 5, 6]
#
# Reorder the nodes of the linked list to be in the following order:
#
# [0, 6, 1, 5, 2, 4, 3]
#
# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
#
# [0, n-1, 1, n-2, 2, n-3, ...]
#
# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
#
# Input: head = [2,4,6,8]
#
# Output: [2,8,4,6]

def reorder_list(head):
    if not head or head.next:
        return
    #find the median
    # [2,4,6,8,10]
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # slow = 6
    # fast = 10

    #reverse the second list
    prev = None
    curr = slow.next # [8,10]
    slow.next =None  # [2,4,6]
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    #list1 = [ 2,4 6]
    #list2 = [10,8]

    first = head
    second = prev

    while second:
        temp1, temp2 = first.next, second.next
        first.next = second  # [2,10]
        second.next = temp1  # [2,10,4]
        first, second = temp1, temp2








