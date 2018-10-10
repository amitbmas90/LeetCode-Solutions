class Solution:
    def maxProduct(self, nums):
        """
        Given an integer array nums, find the contiguous subarray within an array
        (containing at least one number) which has the largest product.
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0

        min_so_far = max_so_far = nums[0]
        res = nums[0]
        for num in nums[1:]:
            max_so_far, min_so_far = (max(num * max_so_far, num * min_so_far, num),
                                    min(num * min_so_far, num * max_so_far, num),
                                    )
            res = max(max_so_far, res)
        return res
