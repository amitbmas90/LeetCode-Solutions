class Solution:
    def numRescueBoats(self, people, limit):
        """
        Each person has to be in one boat. So we have to put heavier people in boats first,
        and then try to squeeze in light weight people.
        Two pointers or shrinking queue would solve this problem.
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        queue = collections.deque(sorted(people))
        count = 0
        while queue:
            count += 1
            last = queue.pop()
            if len(queue) >= 1:
                first = queue[0]
                if first + last <= limit:
                    queue.popleft()
        return count
