def findFinalIndex(nums, index, K):
    """
    type nums: an array of integers of length N. Values are in the range of 0...N-1
    type index: int
    type K: int
    """
    #observation: there exists one and only one cycle from any given index
    if index < 0 or index >= len(nums): return -1
    seen = set()
    cycle = []
    pivot = None

    while K > 0:
        K-=1
        if index == pivot:
            K += 1
            break
        if index in seen:
            if pivot == None:
                pivot = index
            cycle.append(index)

        seen.add(index)
        index = nums[index]
    if K == 0:      # no cycle found
        return index
    print ("Cycle found: ", cycle)
    print ("The number of steps left is %d" % K)
    return cycle[K % len(cycle)]


nums = [1,3,0,1,4,2]
index = 1
K = 5000000
print (findFinalIndex(nums, index, K))
