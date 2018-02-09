# O(N * K) run-time, N is number of strings, O(K) is longest string length
# Space complexity O(N * K)
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c)-ord('a')] += 1
            res[tuple(counts)].append(s)
        return [res[k] for k in res]
