# O(NlogK) run-time and O(K) space complexity for the Priority Queue.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None: return None
        queue = PriorityQueue()
        for l in lists:
            if l != None:
                queue.put((l.val, l))
        dummy = ListNode(0)
        cur = dummy
        while not queue.empty():
            val, node = queue.get()
            cur.next = node
            cur = cur.next
            if node.next:
                queue.put((node.next.val, node.next))
        return dummy.next
  
