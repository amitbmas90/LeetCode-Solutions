# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/problems/reorder-list/description/
# Take care of where to start fast/slow pointers, and how to merge two linked lists
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None: return
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p = slow.next
        slow.next = None    # second half of LL
        t = None            # head of reversed half
        while p:
            temp = p.next
            p.next = t
            t = p
            p = temp
        
        h = head

        while h:
            temp = h.next
            h.next = t
            h = h.next
            t = temp
