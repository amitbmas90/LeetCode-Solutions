# search(word) can search a literal word or a regular expression string containing only letters a-z or '.'. 
# A '.' means it can represent any one letter.
# Idea: Use trie. If the current character is '.', need to search the whole dictionary.
class Node:
    def __init__(self, key = None, data = None):
        self.key = key
        self.children = dict()
        self.data = data
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word == "": return 
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = Node(key = l)
            cur = cur.children[l]
        cur.data = word
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word == "": return False
        def dfs(cur, idx):
            if idx == len(word):
                return cur.data != None
            if word[idx] == '.':
                for k in cur.children:
                    if dfs(cur.children[k], idx+1):
                        return True
                return False
            elif word[idx] not in cur.children:
                return False
            return dfs(cur.children[word[idx]], idx+1)
        return dfs(self.root, 0)
