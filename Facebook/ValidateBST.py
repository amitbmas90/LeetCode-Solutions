# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Recursively solve the problem to avoid falling to trapping test cases.
# e.g. [2147483647,2147483647] and [-2147483648,null,2147483647]
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        stack = []
        prev = None
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev != None and node.val <= prev:
                    return False
                prev = node.val
                node = node.right
        return True
