# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# definitions.
# cur: current list node to visit
# prestart: previous node of the list to reverse
# tail: tail node of reversed list
# temp: node next to tail
# newhead: first node of the reversed portion.
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        count = 0
        prestart = dummy
        while cur != None:
            count += 1
            if count == k:
                temp = cur.next
                newhead = prestart.next
                tail = newhead
                t = newhead.next
                newhead.next = None
                while t != temp:
                    t2 = t.next
                    t.next = newhead
                    newhead = t
                    t = t2
                prestart.next = newhead
                tail.next = temp
                count = 0
                cur = temp
                prestart = tail
                continue
            cur = cur.next
        return dummy.next
