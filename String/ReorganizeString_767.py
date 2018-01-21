class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        heap = [(-S.count(a), a) for a in set(S)]
        if any([-x[0] > (len(S) + 1)//2 for x in heap]): return ''
        heapq.heapify(heap)
        res = []
        
        while len(heap) >= 2:
            cnt1, letter1 = heapq.heappop(heap)
            cnt2, letter2 = heapq.heappop(heap)
            if not res or res[-1] != letter1:
                res.append(letter1)
                res.append(letter2)
                if cnt1 < -1:
                    heapq.heappush(heap, (cnt1+1, letter1))
                if cnt2 < -1:
                    heapq.heappush(heap, (cnt2+1, letter2))
                
        if heap:
            cnt, letter = heapq.heappop(heap)
            res.append(letter)
        return ''.join(res)
