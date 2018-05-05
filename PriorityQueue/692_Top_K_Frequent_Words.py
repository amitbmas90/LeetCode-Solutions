# O(N + klogN) Run-time
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Collections.Counter(words)
        heap = []
        for word, count in counts.items():
            heap.append((-count, word))
        heapify(heap)
        return [heappop(heap) for _ in range(k)]
        
