class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        visited = {i : False for i in range(1, 10)}
        diag = {1: {5}, 2: {4,6}, 3: {5}, 4: {2,8}, 5: {1,2,3,4,6,7,8,9}, 6: {2,8}, 7:{5}, 8: {4,6},
                9: {5}}
        
        def isValid(cur, last):
            if last == -1: return True
            if visited[cur]: return False
            if (cur + last) % 2 == 1: return True   # horizontal or vertical adjacent or knight moves
            if cur in diag[last]: return True
            mid = (cur + last) // 2
            if mid == 5: return visited[mid]
            return visited[mid]
        
        def search(path_len, last):
            if path_len == 0:
                return 1
            res = 0
            for cur in range(1, 10):
                if isValid(cur, last):
                    visited[cur] = True
                    res += search(path_len-1, cur)
                    visited[cur] = False
            return res
                
        for path_len in range(m, n+1):
            for i in range(1,10):
                visited[i] = False
            res += search(path_len, -1)                
        return res
