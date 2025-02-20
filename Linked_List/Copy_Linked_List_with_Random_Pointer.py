# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.
#
# Create a deep copy of the list.
#
# The deep copy should consist of exactly n new nodes, each including:
#
# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.
#
# Return the head of the copied linked list.
#
# Input: head = [[3,null],[7,3],[4,0],[5,1]]
#
# Output: [[3,null],[7,3],[4,0],[5,1]]

def Random_Ptr(head):
    if not head:
        return None

    # Step 1: Create a copy of each node and insert it next to the original node
    curr = head
    while curr:
        newnode = Node(curr.value)
        next = curr.next
        curr.next = newnode
        newnode.next = next
        curr = curr.next.next

    # Step 2: Assign random pointers for the copied nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr.next = curr.next.next

    # Step 3: Separate the original list and the copied list
    old_list = head
    new_list = head.next
    new_head = head.next

    while old_list:
        old_list.next = old_list.next.next
        if new_list:
            new_list.next = new_list.next.next
        old_list = old_list.next
        new_list = new_list.next

    return new_head


