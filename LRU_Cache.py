class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache= {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #1-2 -3--4
    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        self.head.next.prev = node

    # 1-2-3-4
    def remove(self, node):
        prev = node.prev
        next = node.next
        node.prev.next = next
        node.next.prv = prev


    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]

