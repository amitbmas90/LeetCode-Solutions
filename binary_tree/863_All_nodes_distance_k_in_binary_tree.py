# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, parent):
            if node == None:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        # breadth first search
        q = collections.deque([(0, target)])
        res = []
        seen = set()
        while q:
            d, node = q.popleft()
            seen.add(node)
            if d == K:
                res.append(node.val)
            else:
                if node.parent and node.parent not in seen:
                    q.append((d+1, node.parent))
                if node.left and node.left not in seen:
                    q.append((d+1, node.left))
                if node.right and node.right not in seen:
                    q.append((d+1, node.right))
        return res
