class Solution:
    @staticmethod
    def search_range(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search_greater_than(num):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left

        start = search_greater_than(target)
        end = search_greater_than(target + 1) - 1
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, end]


class Solution2:
    @staticmethod
    def search_range(nums, target):
        def search_leftmost(num):
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if nums[mid] < num:
                    left = mid
                else:
                    right = mid
            if nums[left] == num:
                return left
            elif nums[right] == num:
                return right
            return -1

        def search_rightmost(num):
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if nums[mid] > num:
                    right = mid
                else:
                    left = mid
            if nums[right] == num:
                return right
            elif nums[left] == num:
                return left
            return -1

        if len(nums) == 0:
            return [-1, -1]

        start = search_leftmost(target)
        end = search_rightmost(target)

        if start == -1:
            return [-1, -1]
        return [start, end]
