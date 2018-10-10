# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def prune(node):
            # return True if node need to be removed
            if node == None:
                return True, None
            prune_left, left = prune(node.left)
            prune_right, right = prune(node.right)
            node.left, node.right = left, right
            if node.val==0 and prune_left and prune_right:
                return True, None
            return False, node
        
        res, root = prune(root)
        return root
        
