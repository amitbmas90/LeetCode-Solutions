# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []                     # store iterators if the NestedInteger object is list
        self.curIter = iter(nestedList)
        self.curNestedInt = None

    def next(self):
        """
        :rtype: int
        """
        if not self.curNestedInt.isInteger():
            while not self.curNestedInt.isInteger():
                self.stack.append(self.curIter)
                self.curIter = iter(self.curNestedInt.getList())
                self.curNestedInt = next(self.curIter)
        return self.curNestedInt.getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.curNestedInt = next(self.curIter)
        except StopIteration:
            if len(self.stack) == 0:
                return False
            self.curIter = self.stack.pop()
            self.curNestedInt = next(self.curIter)
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
