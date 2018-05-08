class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        slow = 0
        cur, count = None, 0
        for c in chars:
            if cur is None:
                cur = c
            elif c != cur:
                chars[slow] = cur
                slow += 1
                if count > 1:
                    for d in str(count):
                        chars[slow] = d
                        slow += 1
                count = 0
                cur = c
            count += 1
        chars[slow] = cur
        slow += 1
        if count > 1:
            for d in str(count):
                chars[slow] = d
                slow += 1
        return slow
        
