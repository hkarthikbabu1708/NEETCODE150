# Given the beginning of a singly linked list head, reverse the list,
# and return the new beginning of the list.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        curr = self.head

        while curr:
            print(curr.value, end="->")
            curr = curr.next
        print("None")

    def insert(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
        else:
            # this code adds the new node as self.head
            # newnode.next = self.head
            # self.head = newnode

            # this code adds the new node after self.head
            # next = self.head.next
            # self.head.next = newnode
            # newnode.next = next

            # this code adds the new node at the end
            curr = self.head
            while curr and curr.next:
                curr = curr.next
            curr.next = newnode

    def remove(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        # 1 > 2 > 3 > 4
        curr = self.head
        while curr:
            if curr.next.value == value:
                break
            else:
                curr = curr.next
        next = curr.next.next
        curr.next = next

# 1 > 2 > 4
# 1 > 3 > 5
# 1 > 1 > 2 > 3 > 4 > 5
def mergeTwoLists(head1, head2):
    if not head1 and head2:
        return None

    dummy = node = Node()

    while head1 and head2:
        if head1.value < head2.value:
            node.next = head1
            head1 = head1.next
        else:
            node.next = head2
            head2 = head2.next
        node = node.next

    node.next = head1 or head2

    return dummy.next


ll1 = LinkedList()
ll1.insert(1)
ll1.insert(2)
ll1.insert(4)
ll1.print()

ll2 = LinkedList()
ll2.insert(1)
ll2.insert(3)
ll2.insert(5)
ll2.print()

mergeTwoLists(ll1,ll2)


