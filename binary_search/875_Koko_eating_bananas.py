class Solution:
    """Classic binary search (version 2)
        similar to first bad version problem
    """
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        slowest = 1
        fastest = max(piles)
        while slowest < fastest:
            mid = slowest + (fastest - slowest) // 2
            possible = sum([math.ceil(pile / mid) for pile in piles]) <= H
            if possible:
                fastest = mid
            else:
                slowest = mid + 1
        return slowest
