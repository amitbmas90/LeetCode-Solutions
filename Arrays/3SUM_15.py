class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()     # sort inplace
        res = []
        N = len(nums)
        for i in range(N-2):
            if i == 0 or nums[i] > nums[i-1]:
                target = 0 - nums[i]
                j, k = i+1, N-1
                while j < k:
                    if nums[k] + nums[j] == target:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while k > j and nums[k] == nums[k+1]:
                            k -= 1
                    elif nums[k] + nums[j] < target:
                        j += 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                    else:
                        k -= 1
                        while k > j and nums[k] == nums[k+1]:
                            k -= 1
        return res
