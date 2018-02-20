# Trick is to swap value at the end of array with the target to delete and update hash table accordingly.
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.arr = []

        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d: return False
        self.d[val] = len(self.arr)
        self.arr.append(val)
        return True
    
    
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d: return False
        lastnum = self.arr[-1]
        p = self.d[val]
        self.arr[p] = lastnum
        self.d[lastnum] = p
        self.arr.pop()
        self.d.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.arr[random.randrange(len(self.arr))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
