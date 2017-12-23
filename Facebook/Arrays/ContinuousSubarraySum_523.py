# Time-complexity: O(N), space-complecity: O(min(N, k)). 69ms, beat 90.4% Py.
class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0: -1}
        cumSum = 0
        for idx, num in enumerate(nums):
            cumSum += num
            temp = cumSum
            if k != 0:
                temp %= k
            if temp in d:
                if idx - d[temp] > 1:
                    return True
            else:
                d[temp] = idx
        return False
