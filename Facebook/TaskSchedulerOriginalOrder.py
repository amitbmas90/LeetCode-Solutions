# Different from Leetcode 621, this requires tasks to be done in original order.
# In the original problem, order doesn't matter.
def taskScheduler(tasks, idle):
    N = len(tasks)
    total_time = 0
    d = {}          # store latest time execute the same task
    idx = 0         # task waiting to be executed
    while idx < N:
        total_time += 1
        if tasks[idx] not in d:
            d[tasks[idx]] = total_time
            idx += 1
        elif total_time - d[tasks[idx]] > idle:
            d[tasks[idx]] = total_time
            idx += 1
    return total_time

tasks = ['A','A','B','C','B','B','D']
idle = 2
print (taskScheduler(tasks, idle))
