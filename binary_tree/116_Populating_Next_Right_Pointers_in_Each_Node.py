class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        prev = root
        cur = TreeLinkNode(0)

        while prev is not None:
            cur.next = None
            t = cur
            while prev is not None:
                if prev.left:
                    t.next = prev.left
                    t = t.next
                if prev.right:
                    t.next = prev.right
                    t = t.next
                prev = prev.next
            prev = cur.next
