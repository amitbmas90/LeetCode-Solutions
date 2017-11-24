# search(word) can search a literal word or a regular expression string containing only letters a-z or '.'. 
# A '.' means it can represent any one letter.
# Idea: Use trie. If the current character is '.', need to search the whole dictionary.
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        d = self.trie
        for w in word:
            if w in d:
                d = d[w]
            else:
                d[w] = {}
                d = d[w]
        d['*'] = {}
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(word, d):
            if len(word) == 0:
                if '*' in d: return True
                else: return False
            if word[0] == '.':
                for k in d:
                    if dfs(word[1:], d[k]):
                        return True
                return False
            elif word[0] not in d:
                return False
            else:
                return dfs(word[1:], d[word[0]])
        return dfs(word, self.trie)
