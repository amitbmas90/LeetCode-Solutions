# Leetcode 209.
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0: return 0
        N = len(nums)
        
        # accumulated sum in [0, i]
        sums = [0] * N
        sums[0] = nums[0]
        res = float('inf')
        for i in range(1,N):
            sums[i] = sums[i-1] + nums[i]

        for i in range(N):
            # Binary search. Searching for largest j such that sums[i] - sums[j] >= s
            index = bisect.bisect(sums, sums[i] - s, 0, i-1)
            if index > 0:
                res = min(res, i-index+1)
            elif sums[i] >= s:
                res = min(res, i+1)
        return 0 if res == float('inf') else res
