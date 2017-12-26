# A clever grouping made things faster. 
# Instead of calculating each pair of numbers and summing up the distances, we can sum up the total distances of each bit.
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = [0] * 32           # 32-bit integer
        n = len(nums)
        for num in nums:
            k = 0
            while num > 0:
                counts[k] += num & 1
                k += 1
                num >>= 1

        res = sum(count*abs(n-count) for count in counts)
        return res
