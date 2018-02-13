# Leetcode 209.
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.

# Sliding window, O(N) run-time
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = sys.maxsize
        l, winSum = 0, 0
        for i, num in enumerate(nums):
            winSum += num
            while l <= i and winSum >= s:
                res = min(res, i - l + 1)
                winSum -= nums[l]
                l += 1            
        return res if res < sys.maxsize else 0

# O(N*LogN) solution
from bisect import bisect_right
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        cumsums = [0] * (len(nums)+1)
        res = sys.maxsize
        for i, num in enumerate(nums, 1):
            cumsums[i] = cumsums[i-1] + num
            j = bisect_right(cumsums, cumsums[i]-s, 1, i+1)
            if i >= j > 1:
                res = min(res, i - (j - 1))
            elif cumsums[i] >= s:
                res = min(res, i)

        return res if res < sys.maxsize else 0
