class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def rangeSearcher(nums, target, l, r, left):
            while l <= r:
                m = l + (r-l)//2
                if nums[m] > target or left and nums[m] == target:
                     r = m - 1
                else:
                     l = m + 1
            return l if left else r

        if nums == None or len(nums) == 0: return [-1, -1]
        if target < nums[0] or target > nums[-1]: return [-1, -1]

        l = rangeSearcher(nums, target, 0, len(nums)-1, True)
        r = rangeSearcher(nums, target, 0, len(nums)-1, False)
        if nums[l] == target:
            return [l, r]
        return [-1, -1]
        
