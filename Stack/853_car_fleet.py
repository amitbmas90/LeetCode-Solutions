# O(NlogN) run-time, dominated by sort operation.
# O(N) space complexity.
# one confusion in the problem description is the speed when two cars collide follows the slow one
class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time_to_finish = []
        for p, s in sorted(zip(position, speed)):
            time_to_finish.append((target - p) / s)
        stack = []
        for time in time_to_finish[::-1]:
            if len(stack) == 0:
                stack.append(time)
            elif time > stack[-1]:
                    stack.append(time)
        return len(stack)
