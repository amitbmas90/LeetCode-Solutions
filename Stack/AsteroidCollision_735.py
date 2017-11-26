class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        def helper(stack, val):
            if len(stack) == 0 or val > 0 or stack and stack[-1] < 0:
                stack.append(val)
                return
            if abs(val) < stack[-1]: 
                return
            elif abs(val) == stack[-1]: 
                stack.pop()
                return
            else:
                stack.pop()
                helper(stack, val)
                
        for a in asteroids:
            helper(stack, a)
            
        return stack
