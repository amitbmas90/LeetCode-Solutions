# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def find_height(node):
            if node is None:
                return 0
            height = max(find_height(node.left), find_height(node.right)) + 1
            node.height = height
            return height

        def find_node_equal_height(node):
            if node.left == node.right == None:
                return node
            elif node.left is None:
                return find_node_equal_height(node.right)
            elif node.right is None:
                return find_node_equal_height(node.left)
            elif node.left.height == node.right.height:
                return node
            elif node.left.height > node.right.height:
                return find_node_equal_height(node.left)
            else:
                return find_node_equal_height(node.right)

        find_height(root)
        return find_node_equal_height(root)
