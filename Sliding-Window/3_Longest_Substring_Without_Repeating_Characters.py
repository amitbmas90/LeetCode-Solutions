class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        res = 0
        counter = collections.Counter()
        for right, letter in enumerate(s):
            if counter[letter] == 1:
                while left <= right and s[left] != letter:
                    counter[s[left]] -= 1
                    left += 1
                left += 1
            counter[letter] = 1
            res = max(res, right - left + 1)
        return res
