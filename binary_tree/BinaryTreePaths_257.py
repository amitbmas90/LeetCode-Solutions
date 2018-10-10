# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def findPath(path, node):
            if node == None: return
            if node.left == node.right == None:
                if path == "":
                    res.append(str(node.val))
                else:
                    res.append(path + str(node.val))
                return
            if node.left != None:
                findPath(path + str(node.val) + "->", node.left)
            if node.right != None:
                findPath(path + str(node.val) + "->", node.right)
        findPath("", root)
        return res
