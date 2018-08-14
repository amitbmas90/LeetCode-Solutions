"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_seen_ix = {}
        for ix, num in enumerate(nums):
            if num not in last_seen_ix or ix - last_seen_ix[num] > k:
                last_seen_ix[num] = ix
            else:
                return True
        return False
