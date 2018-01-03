class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0: -1}
        cumsum = 0
        I, J = -1, -1
        for i, num in enumerate(nums):
            cumsum += num
            if cumsum - k in d and i - d[cumsum-k] > J - I: 
                    I = d[cumsum-k]
                    J = i
            if cumsum not in d:
                d[cumsum] = i
        return J - I
