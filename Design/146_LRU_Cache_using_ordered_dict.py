# Use Move_to_end function of OrderedDict only available in Python3, and this is faster compared with pop()+append key,val pair
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.od = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.od: return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.od:
            self.od.move_to_end(key)
        elif len(self.od) == self.cap:
            self.od.popitem(last = False)
        self.od[key] = value
