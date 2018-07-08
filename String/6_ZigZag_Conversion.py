class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arrays=[[] for _ in range(numRows)]
        middle = max(numRows-2, 0)
        for idx, char in enumerate(s):
            position = idx % (numRows + middle)
            if position < numRows:
                arrays[position].append(char)
            else:
                arrays[-(position-numRows+2)].append(char)
        return ''.join([''.join(array) for array in arrays])
    