class Solution:
    def stoneGame(self, piles):
        """
        Special DP in the sense of you need to pass state value in recursion.
        :type piles: List[int]
        :rtype: bool
        """
        total = sum(piles)
        memo = {}

        def dp(i, j, cur_sum):
            if (i, j) not in memo:
                if i > j:
                    if total < cur_sum * 2:
                        res = True
                    else:
                        res = False
                else:
                    case1 = dp(i + 1, j - 1, cur_sum + piles[i])
                    case2 = dp(i + 2, j, cur_sum + piles[i])
                    case3 = dp(i + 1, j - 1, cur_sum + piles[j])
                    case4 = dp(i, j - 2, cur_sum + piles[j])
                    res = any([case1, case2, case3, case4])
                memo[i, j] = res
            return memo[i, j]

        return dp(0, len(piles) - 1, 0)
