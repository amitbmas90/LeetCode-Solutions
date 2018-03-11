class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured == 0: return 0.0
        amount = [poured]
        for i in range(1, query_row+1):
            new_amount = [0.0] * (i+1)
            for i, a in enumerate(amount):
                new_amount[i] += 1/2 * max(a - 1, 0)
                new_amount[i+1] += 1/2 * max(a - 1, 0)
            amount = new_amount
            if all([k == 0.0 for k in amount]): return 0.0
        return min(1.0, amount[query_glass])
