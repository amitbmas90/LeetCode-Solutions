# ac 17/17, 89ms
class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search(target):
            if target not in d:
                res = 0
                for num in nums:
                    if num <= target:
                        res += search(target-num)
                d[target] = res
            return d[target]
    
        d = {0: 1}
        return search(target)
