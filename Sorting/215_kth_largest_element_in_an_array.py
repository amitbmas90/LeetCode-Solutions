import random


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target_ix = len(nums) - k
        self.randomization(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            ix = self.quick_select(nums, left, right)
            if ix == target_ix:
                return nums[ix]
            elif ix > target_ix:
                right = ix - 1
            else:
                left = ix + 1
        return 0

    def quick_select(self, nums, i, j):
        """
        nums: list[int]
            array
        i: int
            left boundary of array
        j: int
            right boundary of array
        return: int
            index of pivot after quick select operation
        """
        pivot = nums[j]
        r = i - 1
        for k in range(i, j):
            if nums[k] <= pivot:
                r += 1
                self.swap(nums, r, k)
        r += 1
        self.swap(nums, r, j)
        return r

    def randomization(self, nums):
        for ix, num in enumerate(nums):
            prev = random.randrange(ix + 1)
            self.swap(nums, prev, ix)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
