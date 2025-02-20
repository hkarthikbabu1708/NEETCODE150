# Given the beginning of a singly linked list head, reverse the list,
# and return the new beginning of the list.

class Node:
    def __init__(self,value):
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
            #this code adds the new node as self.head
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

    def rev(self):
        curr = self.head
        prev = None
        next = None
        # 1 > 2 > 3 > 4
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def remove_duplicates(self):
        curr = self.head
        prev = None

        while curr:
            if curr.value == curr.next.value:
                curr.next = curr.next.next

ll = LinkedList()
ll.insert(1)
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
# ll.print()
# ll.remove(4)
# ll.print()
# ll.insert(4)
# ll.print()
# ll.rev()
# ll.print()
# ll.rev()
ll.print()
