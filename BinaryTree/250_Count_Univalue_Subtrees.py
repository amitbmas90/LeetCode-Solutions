# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        def search(node):
            """
            Recursive post-order traversal
            :rtype: bool, True if subtree rooted at node is uni-value
            """
            nonlocal res
            if node.left is None and node.right is None:
                res += 1
                return True
            left_is_unival, right_is_unival= True, True
            if node.left:     left_is_unival = search(node.left)
            if node.right:    right_is_unival = search(node.right)
            if left_is_unival and node.left and node.val != node.left.val: return False
            if right_is_unival and node.right and node.val != node.right.val: return False
            if left_is_unival and right_is_unival:
                res += 1
                return True
            return False
        if root is None: return res
        search(root)
        return res
