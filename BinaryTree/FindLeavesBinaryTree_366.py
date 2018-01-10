# Time-complexity: O(N)
# Space-complexity: O(N)
class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def isLeave(node):
            return node and node.left == node.right == None
        if root == None: return []
        q = collections.deque()
        res = []
        while not isLeave(root):
            cur = []
            q.clear()
            q.append(root)
            while q:
                node = q.popleft()
                if isLeave(node):
                    cur.append(node.val)
                else:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    if isLeave(node.left): node.left = None
                    if isLeave(node.right): node.right = None
            res.append(cur)
        res.append([root.val])
        return res
