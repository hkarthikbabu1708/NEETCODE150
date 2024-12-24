# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
#
# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise,
# add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its
# capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        # head -----node--n1--tail
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        self.head.next.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key):
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.add(self.hash_map[key])
            return self.hash_map[key].val
        return -1

    def put(self, key, val):
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        self.hash_map[key] = ListNode(key,val)
        self.add(self.hash_map[key])

        if len(self.hash_map) > self.capacity:
            lru = self.tail.prev
            self.remove(self.hash_map[lru.key])
            del self.hash_map[lru.key]

lru = LRUCache(2)
print(lru)
lru.put(1,10)
print(lru.get(1))
lru.put(2,20)
lru.put(3,30)
print(lru.get(1))
print(lru.get(2))


