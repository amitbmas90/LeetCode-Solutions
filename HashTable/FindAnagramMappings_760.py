# Time-complexity O(N), space-complexity O(N), N is size of A or B.
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        memo = collections.defaultdict(list)    # saving indexes to lists to deal with duplication
        for idx, num in enumerate(B):
            memo[num].append(idx)     
        return [memo[num].pop() for num in A]
