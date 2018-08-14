class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        def dfs(start, path):
            if start == len(nums): return
            for i in range(start, len(nums)):
                res.append(list(path+[nums[i]]))
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
