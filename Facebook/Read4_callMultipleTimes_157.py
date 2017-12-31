# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buffer = ['a'] * 4
        res = 0
        while res < n:
            count = read4(buffer)
            temp = n - res
            for i in range(min(count, temp)):
                buf[res] = buffer[i]
                res += 1
            if count < 4: break
        return res
