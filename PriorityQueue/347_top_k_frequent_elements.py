# O(Nlogk) run-time and O(k) space-complexity.
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        heap = [counts.popitem()[::-1] for _ in range(k)]
        heapq.heapify(heap)
        for key, val in counts.items():
            if val > heap[0][0]:
                heapq.heapreplace(heap, (val, key))
        return sorted([x[1] for x in heap])
        
