# The problem should state the assumption that the more difficult the job, the higher profit.
# O(JlogJ+WlogW) run-time, where J is number of jobs and W is number of workers. Run-time is dominated by sorting.
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        res = 0
        most_diff = 0
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        best = 0
        for work in sorted(worker):
            while most_diff < len(jobs) and work >= jobs[most_diff][0]:
                best = max(best, jobs[most_diff][1])
                most_diff += 1
            res += best
        return res
        
