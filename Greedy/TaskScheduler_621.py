# This greedy solution needs mathematical proof.
# We need to get two stats: F, maximum count of any task. M, number of tasks with this count.
# So the number of tasks with this count <= N / F, where N is the total number of tasks. If cooldown n >= N / F, then n >= M.
# This implies that all the most frequent tasks can be inserted in the group with size (n+1).
# Conversely, if n < N / F, then the group size is too small. We should return N.
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        M = F = 0
        T = {}
        for task in tasks:
            if task in T:
                T[task] += 1
            else:
                T[task] = 1
            if T[task] > F:
                F = T[task]
                M = 1
            elif T[task] == F:
                M += 1
        if n >= len(tasks) // F:
            return M + (F-1) * (n + 1)
        return len(tasks)
