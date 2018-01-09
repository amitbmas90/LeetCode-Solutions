# The trap here is when using the buffer to push back smaller numbers, the new max need to be updated. The push helper does the work.
# Python version of the smart solution by @inofance
# Ref: https://leetcode.com/problems/max-stack/discuss/108938
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_ = []
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.pushhelper(x)
    
    def pushhelper(self, x):
        temp_max = -sys.maxsize if not self.max_ else self.max_[-1] # get maximum in the stack
        if x > temp_max:
            temp_max = x
        
        self.stack.append(x)
        self.max_.append(temp_max)
        
        
    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            res = self.stack.pop()
            self.max_.pop()
            return res

        
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        if self.max_:
            return self.max_[-1]

    def popMax(self):
        """
        :rtype: int
        """
        buffer = []
        res = self.max_[-1]
        while self.stack and self.stack[-1] != self.max_[-1]:
            self.max_.pop()
            buffer.append(self.stack.pop())
        
        self.stack.pop()
        self.max_.pop()

        while buffer:
            self.pushhelper(buffer.pop())
        return res
