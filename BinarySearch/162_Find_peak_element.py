class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > max(nums[mid - 1], nums[mid + 1]):
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid
            else:
                left = mid

        if nums[left] > nums[left + 1] and (left == 0 or nums[left] > nums[left - 1]):
            return left
        if nums[right] > nums[right - 1] and (right == len(nums) - 1 or nums[right] > nums[right + 1]):
            return right
        return -1
