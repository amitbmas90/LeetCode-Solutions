class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -sys.maxsize
        counter = collections.Counter()  # stores at most two distinct characters
        start = 0
        for end, c in enumerate(s):
            counter[c] += 1
            while start < end and len(counter) > 2:
                cur = s[start]
                counter[cur] -= 1
                if counter[cur] == 0:
                    counter.pop(cur)
                start += 1
            res = max(res, end - start + 1)
        return res if res > -sys.maxsize else 0
