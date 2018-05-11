class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: 
            return 0
            
        res = 0
        water = [0] * len(height)
        left_max, right_max = 0, 0
        
        for idx, h in enumerate(height):
            left_max = max(left_max, h)
            water[idx] = left_max
            
        for idx, h in enumerate(height[::-1], 1):
            right_max = max(right_max, h)
            water[-idx] = max(min(water[-idx], right_max) - height[-idx], 0)
            res += water[-idx]
            
        return res
