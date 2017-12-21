# Insertion-based iterative method is more intuitive.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        N = len(nums)
        def dfs(path, idx):
            if idx == N:
                res.append(list(path))
                return
            for i in range(idx, N):
                nums[idx], nums[i] = nums[i], nums[idx]
                dfs(path + [nums[idx]], idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        dfs([], 0)
        return res
