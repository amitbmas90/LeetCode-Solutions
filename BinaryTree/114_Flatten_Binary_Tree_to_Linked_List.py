# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None: return
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if prev is not None:
                prev.right = node
                prev.left = None
            prev = node
            if node.left:
                stack.append(node.left)
