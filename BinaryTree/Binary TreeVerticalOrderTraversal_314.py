# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        d = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            cur, col = queue.popleft()
            if cur.left: queue.append((cur.left, col-1))
            if cur.right: queue.append((cur.right, col+1))
            d[col].append(cur.val)
        return [d[k] for k in sorted(d.keys())]
