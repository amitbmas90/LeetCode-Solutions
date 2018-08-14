import collections


class Solution:
    def topKFrequent(self, nums, k):
        """
        O(N) run-time and O(N) space complexity, where N is number of numbers in the list
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        N = len(nums)
        frequencies = [list() for _ in range(N + 1)]

        for num, freq in counter.items():
            frequencies[N - freq].append(num)

        res = []
        it = iter(frequencies)
        while len(res) < k:
            next_list = next(it)
            max_ = min(k - len(res), len(next_list))
            res.extend(next_list[:max_])
        return res
