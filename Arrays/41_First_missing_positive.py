class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        for ix, num in enumerate(nums):
            if num <= 0:
                nums[ix] = N + 2  # N + 2 can never be the first missing positive

        for num in nums:
            temp = abs(num)
            if temp <= N and nums[temp - 1] > 0:
                nums[temp - 1] = -nums[temp - 1]

        for ix, num in enumerate(nums):
            if num > 0:
                return ix + 1

        return N + 1
