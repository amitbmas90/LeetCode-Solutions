# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        Smart thief realized houses form a binary tree.
        It will automatically contact the police if two directly-linked houses were broken into on the same night.
        Determine maximum value thief can rob without alerting police.
        :type root: TreeNode
        :rtype: int
        """
        def search(node):
            if node is None: return (0, 0)  # include / exclude node
            l = search(node.left)
            r = search(node.right)
            include_node = node.val + l[1] + r[1]
            exclude_node = max(l) + max(r)
            return (include_node, exclude_node)
        return max(search(root))
