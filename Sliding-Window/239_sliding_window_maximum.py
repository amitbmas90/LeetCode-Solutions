import collections


class Solution:
    def max_sliding_window(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = collections.deque()
        n = len(nums)

        for i in range(n):
            while q and q[-1][1] <= nums[i]:
                q.pop()
            q.append((i, nums[i]))

            if i >= k:
                while q and q[0][0] <= i - k:
                    q.popleft()

            if i >= k - 1:
                res.append(q[0][1])
        return res
