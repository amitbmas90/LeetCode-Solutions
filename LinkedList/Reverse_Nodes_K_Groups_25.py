# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Clear definition of start and end.
# start: first node before the partition need to be reversed
# end: first node after the partition need to be reversed
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        count = 0
        end = start.next
        while end != None:
            count = 0
            while count < k and end != None:
                count += 1
                end = end.next          
            if count == k:  # reverse start to end
                reversedList = None
                temp = start.next
                while temp != end:
                    # print (temp.val)
                    temp2 = temp.next
                    temp.next = reversedList
                    reversedList = temp
                    # print (reversedList.val)
                    temp = temp2
                start.next = reversedList
                while reversedList.next:
                    reversedList = reversedList.next
                start = reversedList
                reversedList.next = end

        return dummy.next
