class Solution:
    def buildTree(self, preorder, inorder):
        """
        first node in pre-order must be root.
        find this value in in-order, and this value shall be the middle of left in-order
        and right in-order.
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])

        root_ix = inorder.index(preorder[0])

        left_inorder, right_inorder = inorder[:root_ix], inorder[root_ix + 1:]
        left_preorder, right_preorder = preorder[1: root_ix + 1], preorder[root_ix + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
