# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = float('inf')
        val = None

        def search(node):
            nonlocal res, val
            if node is None:
                return
            if res > abs(target - node.val):
                val = node.val
                res = abs(target - node.val)
            if node.val < target:
                search(node.right)
            else:
                search(node.left)

        search(root)
        return val
