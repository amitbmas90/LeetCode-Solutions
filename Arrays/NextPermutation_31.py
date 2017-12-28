# added binary search to search range j+1 to n, but speed is not improving. Maybe it's because O(N)+O(logN) ~= 2*O(N)
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def binSearch(arr, l, r, t):
            while l <= r:
                m = l + (r-l) // 2
                if arr[m] <= t:
                    r = m - 1
                else:
                    l = m + 1
            return r
        n = len(nums)
        j = n-2
        while j >= 0:
            if nums[j] < nums[j+1]:
                break
            j-=1

        if j >= 0:
            i = binSearch(nums, j+1, n-1, nums[j])
            nums[i], nums[j] = nums[j], nums[i]
        nums[j+1:] = nums[j+1:][::-1]
