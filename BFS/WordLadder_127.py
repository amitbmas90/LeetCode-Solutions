# This is basic undirected graph BFS. Should use regular deque
import string
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    words = set(wordList)
    lowercaseletters = set(string.ascii_lowercase)

    queue = deque();
    queue.append((1, beginWord))

    while queue:
        d, word = queue.popleft()
        if word == endWord:
            return d
        for i in range(len(word)):
            for lcl in lowercaseletters:
                newWord = word[:i] + lcl + word[i+1:]
                if newWord in words:
                    words.remove(newWord)
                    queue.append((d + 1, newWord))
    return 0

beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog", "dom"]
print (ladderLength(beginWord, endWord, wordList))
