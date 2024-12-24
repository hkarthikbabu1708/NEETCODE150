# Given the beginning of a linked list head, return true if there is a
# cycle in the linked list. Otherwise, return false.

def detectCycle(head):
    if not head:
        return False

    fast = head
    slow = head

    while fast:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False



