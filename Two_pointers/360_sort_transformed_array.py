import bisect


class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def calculate(x):
            return a * x * x + b * x + c

        if b == 0:
            m = 0
        elif a == 0:
            if b > 0:
                return list(map(lambda x: b * x + c, nums))
            else:
                return list(map(lambda x: b * x + c, nums))[::-1]
        else:
            m = -b / (2 * a)

        m_ix = bisect.bisect(nums, m)
        left, right = m_ix - 1, m_ix

        if a < 0:
            nums[:m_ix] = nums[:m_ix][::-1]
            nums[m_ix:] = nums[m_ix:][::-1]

        res = []
        while left >= 0 and right < len(nums):
            left_val, right_val = calculate(nums[left]), calculate(nums[right])
            if left_val <= right_val:
                res.append(left_val)
                left -= 1
            else:
                res.append(right_val)
                right += 1

        while left >= 0:
            res.append(calculate(nums[left]))
            left -= 1

        while right < len(nums):
            res.append(calculate(nums[right]))
            right += 1

        return res
