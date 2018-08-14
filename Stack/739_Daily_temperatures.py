class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)
        for ix, temp in enumerate(temperatures[::-1]):
            while stack and stack[-1][1] <= temp:
                stack.pop()
            if len(stack) == 0:
                continue
            else:
                res[ix] = ix - stack[-1][0]
            stack.append((ix, temp))
        return res
