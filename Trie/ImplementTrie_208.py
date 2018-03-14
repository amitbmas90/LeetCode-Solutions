# Since the problem states that input only contains lower-case letters, 
# we can use array to store children instead of Dict or HashMap to accelerate search.
class TrieNode:
    def __init__(self, prefix = None, isWord = False):
        self.prefix = prefix
        self.isWord = isWord
        self.children = [None] * 26
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(prefix = '')


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        path = []
        for c in word:
            path.append(c)
            temp = ord(c) - ord('a')   
            if not cur.children[temp]:
                cur.children[temp] = TrieNode(prefix = ''.join(path))
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
        return start.isWord
    

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
