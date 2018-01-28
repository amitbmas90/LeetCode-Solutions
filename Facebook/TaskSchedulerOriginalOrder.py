# Different from Leetcode 621, this requires tasks to be done in original order.
# In the original problem, order doesn't matter.
def taskScheduler(tasks, n):
    d = {}
    time = 0
    for task in tasks:
        time += 1
        if task not in d or time - d[task] > n:
            d[task] = time
        else:
            time = d[task] + n + 1
            d[task] = time
    return time

tasks = ['A','A','B','C','B','B','D']
idle = 2
print (taskScheduler(tasks, idle))
