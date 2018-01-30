# Resovior Sampling
# This is faster than Java version! Python Random module is highly optimized!
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count, res = 0, 0
        for i, num in enumerate(self.nums):
            if num != target: continue
            if random.randint(0, count) == 0:
                res = i
            count += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
