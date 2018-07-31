class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        num_zeros = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 0:
                num_zeros += 1
            while num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        res = max(res, right - left + 1)
        return res
