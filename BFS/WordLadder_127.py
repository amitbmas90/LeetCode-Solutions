from queue import PriorityQueue
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        visited = {word: False for word in wordList if word != beginWord}
        lowercaseletters = set(string.ascii_lowercase)
        q = PriorityQueue();
        q.put((1, beginWord))
        while not q.empty():
            d, word = q.get()
            if word != beginWord and visited[word]: continue
            if word == endWord:
                return d
            visited[word] = True
            for i in range(len(word)):
                for lcl in lowercaseletters:
                    newWord = word[:i] + lcl + word[i+1:]
                    if newWord in visited and not visited[newWord]:
                        q.put((d+1, newWord))
        return 0
                    
