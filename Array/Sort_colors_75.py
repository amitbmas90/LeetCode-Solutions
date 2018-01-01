// Given an array with n objects colored red, white or blue, 
// sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
// Try to do with one pass time complexity and O(1) extra space.
// Define [0, i] be color red, [i+1, j] be color white, and [j+1, k] be color blue. k is iterator index.

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = -1
        for k, v in enumerate(nums):
            if v < 2:
                j += 1
                nums[j] = 1
                if v == 0:
                    i += 1
                    nums[i] = 0
            if k > j:
                nums[k] = 2
