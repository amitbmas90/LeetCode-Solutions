class Solution:
    def kthSmallest(self, root, k):
        """
        1 <= k <= number of nodes in the tree
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
        return 0


class Solution2:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def count(node):
            if node is None:
                return 0
            return count(node.left) + count(node.right) + 1

        left_count = count(root.left)

        if left_count >= k:
            return self.kthSmallest(root.left, k)
        elif left_count < k - 1:
            return self.kthSmallest(root.right, k - left_count - 1)

        return root.val
