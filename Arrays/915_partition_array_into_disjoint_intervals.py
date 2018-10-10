class Solution:
    def partitionDisjoint(self, A):
        """
        Description:
            https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
        :type A: List[int]
        :rtype: int
        """
        left_lsf, left_largest = -float('inf'), []
        right_ssf, right_smallest = float('inf'), []

        for num in A:
            if left_lsf < num:
                left_largest.append(num)
                left_lsf = num
            else:
                left_largest.append(left_lsf)

        for num in A[::-1]:
            if right_ssf > num:
                right_smallest.append(num)
                right_ssf = num
            else:
                right_smallest.append(right_ssf)

        right_smallest = right_smallest[::-1]

        for i in range(len(A) - 1):
            if left_largest[i] <= right_smallest[i + 1]:
                return i + 1
