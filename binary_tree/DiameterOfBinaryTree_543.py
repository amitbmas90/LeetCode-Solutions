class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        def depth(root):
            nonlocal res
            if root == None:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            res = max(res, l + r)
            return max(l, r) + 1
        depth(root)
        return res
