class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        # m < n
        start, prev = head, None
        count = m - 1
        # Find start of segment needs reverse
        while count > 0:
            prev = start
            start = start.next
            count -= 1
        
        last = start                # save the tail
        # Reverse segment
        count = n - m + 1
        newHead, temp = None, None
        while count > 0:
            temp = start.next
            start.next = newHead
            newHead = start
            start = temp
            count -= 1
            
        last.next = temp
        if prev:
            prev.next = newHead
            return head
        else:
            return newHead
