# Solution inspired by C++ solution from @LUCASTAN
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        start, end = 0, N-1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        rot = start
        start, end = 0, N-1
        while start <= end:
            mid = start + (end-start) // 2
            trueMid = (mid + rot) % N
            if nums[trueMid] == target:
                return trueMid
            elif nums[trueMid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
