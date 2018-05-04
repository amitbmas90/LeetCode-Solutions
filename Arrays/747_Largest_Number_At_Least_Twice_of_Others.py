class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, second = 0, -1
        for i, num in enumerate(nums):
            if i == 0:
                largest = 0
            elif nums[largest] < nums[i]:
                largest, second = i, largest
            elif second == -1 or nums[second] < nums[i]:
                second = i
        if second == -1 or nums[second] * 2 <= nums[largest]: return largest
        return -1
        
