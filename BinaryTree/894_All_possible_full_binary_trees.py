# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        memo = {1: [TreeNode(0)]}

        def build(n):
            """
            return all possible FBT with n nodes
            """
            if n not in memo:
                res = []
                if n % 2 != 0:
                    for i in range(1, n - 1):
                        left = i
                        right = n - 1 - i
                        if left % 2 == 1 and right % 2 == 1:
                            left_ = build(left)
                            right_ = build(right)
                            for l in left_:
                                for r in right_:
                                    new_tree = TreeNode(0)
                                    new_tree.left, new_tree.right = l, r
                                    res.append(new_tree)
                memo[n] = res
            return memo[n]

        return build(N)
