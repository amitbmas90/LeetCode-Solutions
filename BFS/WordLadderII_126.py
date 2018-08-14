# Inspired by Java solution from @CHENGZHANG
import collections, string


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        distances = {beginWord: 0}
        neighbors = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(beginWord)
        res = []

        def findNeighbors(word):
            for k, c in enumerate(word):
                for m in set(string.ascii_lowercase):
                    if m != c:
                        newWord = word[:k] + m + word[k + 1:]
                        if newWord in wordList:
                            neighbors[word].append(newWord)
        foundEnd = False
        while queue:
            cnt = len(queue)
            while cnt > 0:
                cnt -= 1
                cur = queue.popleft()
                findNeighbors(cur)
                for neighbor in neighbors[cur]:
                    if neighbor not in distances:
                        distances[neighbor] = distances[cur] + 1
                        if neighbor == endWord:
                            foundEnd = True
                        else:
                            queue.append(neighbor)
                if foundEnd: break

        def findResults(path, cur):
            if cur == endWord:
                res.append(path)
            else:
                for neighbor in neighbors[cur]:
                    if neighbor in distances and distances[neighbor] == distances[cur] + 1:
                        findResults(path + [neighbor], neighbor)

        findResults([beginWord], beginWord)
        return res
