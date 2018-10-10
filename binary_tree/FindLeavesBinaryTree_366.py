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

    
# Resursion inspired by Java solution by @sky-xu on Leetcode discussion
class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node):
            if node == None: return -1
            height = 1 + max(dfs(node.left), dfs(node.right))
            if height + 1 > len(res): res.append(list())
            res[height].append(node.val)
            node.left = None
            node.right = None
            return height
        dfs(root)
        return res
