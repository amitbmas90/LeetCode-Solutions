class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_path = []
        t_path = []

        self.preorder(s, s_path)
        self.preorder(t, t_path)

        s_string = ' '.join(s_path)
        t_string = ' '.join(t_path)
        index = s_string.find(t_string)

        return index != -1 and (index == 0 or s_string[index - 1] == ' ')

    def preorder(self, root, path):
        if root is None:
            path.append('#')
            return
        path.append(str(root.val))
        self.preorder(root.left, path)
        self.preorder(root.right, path)
