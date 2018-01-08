# Runtime: O(n) init and O(nlogn) query.
# There is O(n) query solution which is faster. Two pointers pointing to two lists. 
# A[i] < B[j]: i+=1 else j+=1, collecting minimum along the way.
from bisect import bisect
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordpos = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.wordpos[word].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = sys.maxsize
        if len(self.wordpos[word1]) > len(self.wordpos[word2]):
            return self.shortest(word2, word1)
        for idx in self.wordpos[word1]:
            p = bisect(self.wordpos[word2], idx)
            if p == 0:
                res = min(res, self.wordpos[word2][0]-idx)
            elif p == len(self.wordpos[word2]):
                res = min(res, idx - self.wordpos[word2][-1])
            else:
                res = min(res, idx - self.wordpos[word2][p-1], abs(self.wordpos[word2][p] - idx))
        return res
