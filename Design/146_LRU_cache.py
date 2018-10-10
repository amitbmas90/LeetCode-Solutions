class Listnode:
    """
    doubly linked list node
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        need one linked list and a hash map
        :type capacity: int
        """
        self.map = {}
        self.head = Listnode(0, 0)
        self.tail = Listnode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.node_count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        self.move_to_head(self.map[key])
        return self.map[key].val

    def insert_to_head(self, node):
        temp = self.head.next

        self.head.next = node
        node.prev = self.head

        temp.prev = node
        node.next = temp

    @staticmethod
    def remove(node):
        prev = node.prev
        next_ = node.next

        prev.next = next_
        next_.prev = prev

        node.prev = node.next = None

    def move_to_head(self, node):
        LRUCache.remove(node)
        self.insert_to_head(node)

    def remove_from_tail(self):
        node = self.tail.prev
        prev = node.prev

        prev.next = self.tail
        self.tail.prev = prev

        node.prev = node.next = None

        # remove from map
        self.map.pop(node.key)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            self.map[key].val = value
            self.move_to_head(self.map[key])
        else:
            self.map[key] = Listnode(key, value)
            if self.node_count == self.capacity:
                # remove lru node and insert new node
                self.remove_from_tail()
                self.insert_to_head(self.map[key])
            else:
                self.node_count += 1
                self.insert_to_head(self.map[key])
