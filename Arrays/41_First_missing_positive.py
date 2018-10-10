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


import sys
class Solution_2:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far = sys.maxsize
        for i, num in enumerate(nums):
            if num < 0:
                # we don't care negatives, set them to 0
                nums[i] = 0
            if num > 0:
                min_so_far = min(min_so_far, num)

        if min_so_far > 1:
            # quickly check if minimum positive is greater than 1.
            # if yes, return 1
            return 1

        for i, num in enumerate(nums):
            temp = abs(num)
            if temp > 0 and temp <= len(nums):
                if nums[temp - 1] == 0:
                    nums[temp - 1] = -temp
                elif nums[temp - 1] > 0:
                    nums[temp - 1] *= -1

        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1

        return len(nums) + 1
