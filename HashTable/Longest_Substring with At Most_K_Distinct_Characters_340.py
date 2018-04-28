from collections import Counter
class Solution_1:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0 and len(s) > 0: return 0
        cnt = Counter()
        n = len(s)
        num_distinct, i = 0, 0
        res = 0
        for j in range(n):
            if cnt[s[j]] > 0:
                cnt[s[j]] += 1
            elif num_distinct < k:
                num_distinct += 1
                cnt[s[j]] += 1
            else:
                cnt[s[j]] += 1
                num_distinct += 1
                while i <= j and cnt[s[i]] > 0 and num_distinct > k:
                    cnt[s[i]] -= 1
                    if cnt[s[i]] == 0:
                        num_distinct -= 1
                    i += 1
        return res

class Solution_2:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        def findLongest(start):
            cnt = Counter()
            i = start
            l = 0
            while i < len(s):
                if len(cnt) == k and s[i] not in cnt:
                    return cnt, l
                cnt[s[i]] += 1
                l += 1
                i += 1
            return cnt, l
        if k == 0 and len(s) > 0: return 0
        if len(s) <= k: return len(s)
        last, l = Counter([s[-1]]), 1
        res = l
        for i in range(len(s)-2, -1, -1):
            if l < k or s[i] in last:
                last[s[i]] += 1
                l += 1
            else:
                last, l = findLongest(i)
            res = max(res, l)
        return res
        
