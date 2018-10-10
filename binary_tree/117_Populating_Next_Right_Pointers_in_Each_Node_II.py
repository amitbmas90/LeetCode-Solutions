# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# Solution inspired by C++ solution III in http://www.cnblogs.com/grandyang/p/4290148.html
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        dummy = TreeLinkNode(0)
        next_ = dummy
        cur = root
        while cur:
            if cur.left:
                next_.next = cur.left
                next_ = next_.next
            if cur.right:
                next_.next = cur.right
                next_ = next_.next
            cur = cur.next
            if not cur:
                cur = dummy.next
                next_ = dummy
                dummy.next = None
        
