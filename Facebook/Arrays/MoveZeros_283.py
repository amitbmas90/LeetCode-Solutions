# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = -1
        for j, num in enumerate(nums):
            if num != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
