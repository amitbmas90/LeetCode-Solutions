class Solution:
    def findStrobogrammatic(self, n):
        """
        A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
        Find all strobogrammatic numbers that are of length = n.
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return self.search(1)
        elif n == 2:
            return self.search(2)
        return self.search(n, enable_zero=False)

    def search(self, n, enable_zero=False):
        if n == 1:
            return list('018')
        elif n == 2:
            if enable_zero:
                return ['00', "11", "69", "88", "96"]
            else:
                return ["11", "69", "88", "96"]
        res = []

        if not enable_zero:
            selections = [('6', '9'), ('9', '6'), ('8', '8'), ('1', '1')]
        else:
            selections = [('6', '9'), ('9', '6'), ('8', '8'), ('1', '1'), ('0', '0')]

        subres = self.search(n - 2, enable_zero=True)
        for val in subres:
            for sel in selections:
                res.append(sel[0] + val + sel[1])
        return sorted(res)
