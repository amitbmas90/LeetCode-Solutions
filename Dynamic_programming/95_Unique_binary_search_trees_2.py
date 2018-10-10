# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dp(i, j):
            """
            return all trees built with numbers in [i, j]
            """
            if (i, j) not in trees:
                new_trees = []
                if i <= j:
                    new_trees = []
                    for k in range(i, j + 1):
                        left_trees = dp(i, k - 1)
                        right_trees = dp(k + 1, j)
                        if left_trees and right_trees:
                            for t1 in left_trees:
                                for t2 in right_trees:
                                    new_tree = TreeNode(k)
                                    new_tree.left = t1
                                    new_tree.right = t2
                                    new_trees.append(new_tree)
                        elif left_trees:
                            for t in left_trees:
                                new_tree = TreeNode(k)
                                new_tree.left = t
                                new_trees.append(new_tree)
                        elif right_trees:
                            for t in right_trees:
                                new_tree = TreeNode(k)
                                new_tree.right = t
                                new_trees.append(new_tree)
                        else:
                            new_trees.append(TreeNode(k))
                trees[i, j] = new_trees
            return trees[i, j]

        trees = {}  # mapping index pair to list of binary search trees
        dp(1, n)
        return trees[1, n]
