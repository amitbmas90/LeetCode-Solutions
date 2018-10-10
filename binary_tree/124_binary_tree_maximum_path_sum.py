import sys


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -sys.maxsize
        self.max_path_from_root(root)
        return self.res

    def max_path_from_root(self, root):
        """
        return the maximum sum path from root to leaf
        calculate subproblem of max path that goes through root
        """
        if root is None:
            return 0
        left = max(0, self.max_path_from_root(root.left))
        right = max(0, self.max_path_from_root(root.right))
        self.res = max(self.res, root.val + left + right)
        return root.val + max(left, right)
