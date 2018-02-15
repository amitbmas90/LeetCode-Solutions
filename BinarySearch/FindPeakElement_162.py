# Binary Search version 2 with slight tweak of r == len(nums)-1, this is for the case of all the way increasing sequence.
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l) // 2
            if nums[m+1] > nums[m]:
                l = m + 1
            else:
                r = m
        return l if l != len(nums) else -1
