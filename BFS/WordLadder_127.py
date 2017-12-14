from queue import PriorityQueue
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        visiting = {word: False for word in wordList}
        visited = set()
        words = set(wordList)
        lowercaseletters = set(string.ascii_lowercase)

        q = PriorityQueue();
        q.put((1, beginWord))

        while not q.empty():
            d, word = q.get()
            visited.add(word)
            if word == endWord:
                return d
            for i in range(len(word)):
                for lcl in lowercaseletters:
                    newWord = word[:i] + lcl + word[i+1:]
                    if newWord not in visited:
                        if newWord in words and not visiting[newWord]:
                            q.put((d + 1, newWord))
                            visiting[newWord] = True
        return 0
