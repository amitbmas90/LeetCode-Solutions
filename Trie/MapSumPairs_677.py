"""
-------------
Leetcode #677
-------------
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer).
The string represents the key and the integer represents the value.
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix,
and you need to return the sum of all the pairs' value whose key starts with the prefix.
"""

class MapSum():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val
        cur_dict = self.trie
        for letter in key:
            cur_dict.setdefault(letter, {})
            cur_dict = cur_dict[letter]
        cur_dict["_"] = '_'

    def search(self, prefix):
        # return a list of words with the prefix
        res = []
        cur_dict = self.trie
        for letter in prefix:
            if letter not in cur_dict:
                return []
            cur_dict = cur_dict[letter]
        def dfs(cur_dict, prefix):
            if "_" in cur_dict:
                res.append(prefix)
            for letter in cur_dict:
                temp = cur_dict
                if letter != '_':
                    cur_dict = cur_dict[letter]
                    dfs(cur_dict, prefix+letter)
                    # backtracking
                    cur_dict = temp
        dfs(cur_dict, prefix)
        return res

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        words = self.search(prefix)
        return sum([self.map[w] for w in words])

# Tests
mapSum = MapSum()
mapSum.insert("Beauty", 100)
mapSum.insert("Beast", 87)
mapSum.insert("Print", 50)
mapSum.insert("Princess", 70)

# Expect 187
print (mapSum.sum("Be"))

# Expect 120
print (mapSum.sum("Prin"))
