# Since the problem limit the characters being a-z, we can use array to store children instead of Dict to accelerate.
class TrieNode:
    def __init__(self, key, isWord = False):
        self.key = key
        self.isWord = isWord
        self.children = [None] * 26
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            temp = ord(c) - ord('a')
            if not cur.children[temp]:
                cur.children[temp] = TrieNode(c)
            cur = cur.children[temp]
        cur.isWord = True
        
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        start = self.root
        for c in word:
            temp = ord(c) - ord('a')
            if not start.children[temp]: return False
            start = start.children[temp]
        return True if start.isWord else False
    

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        start = self.root
        for c in prefix:
            temp = ord(c) - ord('a')
            if not start.children[temp]: return False
            start = start.children[temp]
        return True
            

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
