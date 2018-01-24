# Doubly linked lists + HashMap solution
# getMaxKey and getMinKey are not exactly O(1)
class ListNode:
    def __init__(self, key):
        self.key = key
        self.val = 0
        self.next = None
        self.prev = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyNode = {}
        self.valHeads = collections.defaultdict(ListNode)
        self.curmax = 0
        self.curmin = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.keyNode:  # new key
            node = ListNode(key)
            self.keyNode[key] = node
        node = self.keyNode[key]
        node.val += 1
        temp = self.valHeads.get(node.val)

        p = node.prev
        n = node.next
        node.prev = None
        node.next = temp
        if p != None:
            p.next = n
        if n != None:
            n.prev = p
        if self.valHeads.get(node.val - 1) == node:
            self.valHeads[node.val - 1] = n
            if n == None:
                self.valHeads.pop(node.val - 1)
        if self.valHeads.get(node.val):
            self.valHeads[node.val].prev = node
            node.next = self.valHeads[node.val]
        self.valHeads[node.val] = node


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.keyNode:
            return
        node = self.keyNode[key]
        if node.val == 1:
            self.keyNode.pop(key)
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if self.valHeads[node.val] == node:
                self.valHeads[node.val] = node.next
                if node.next == None:
                    self.valHeads.pop(1)
                else:
                    node.next.prev = None
        else:
            node.val -= 1
            temp = self.valHeads.get(node.val)

            p = node.prev
            n = node.next
            node.prev = None
            node.next = temp
            if p != None:
                p.next = n
            if n != None:
                n.prev = p
            if self.valHeads[node.val+1] == node:
                self.valHeads[node.val+1] = n
                if n == None:
                    self.valHeads.pop(node.val + 1)
            if self.valHeads.get(node.val):
                self.valHeads[node.val].prev = node
                node.next = self.valHeads[node.val]
            self.valHeads[node.val] = node


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if len(self.valHeads) == 0: return ""
        return self.valHeads.get(max(self.valHeads)).key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if len(self.valHeads) == 0: return ""
        return self.valHeads.get(min(self.valHeads)).key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
