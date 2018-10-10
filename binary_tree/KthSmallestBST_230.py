# O(N) Run-time and O(N) space-complexity
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # in-order traversal find k-th
        count, res = 0, None
        stack, node = [], root
        while count < k and stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res = node.val
                count += 1
                node = node.right
        return res
