class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder_traversal(node):
            nonlocal prev
            if node is None:
                return True

            left = inorder_traversal(node.left)

            if not left:
                return False

            if prev >= node.val:
                return False

            prev = node.val
            return inorder_traversal(node.right)

        import sys
        prev = -sys.maxsize
        return inorder_traversal(root)
