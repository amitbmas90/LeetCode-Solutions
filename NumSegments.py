def numberSegments(s):
    d = {}
    res = []
    for idx, c in enumerate(s):
        if c not in d:
            d[c] = (idx, idx)
        else:
            d[c] = (d[c][0], idx)

    res = sorted([d[k] for k in d], key = lambda x:x[0])
    newList = []
    for interval in res:
        if not newList or interval[0] > newList[-1][1]:
            newList.append(interval)
        else:
            temp = newList.pop()
            newList.append((min(temp[0], interval[0]), max(temp[1], interval[1])))

    return len(newList)

s = list("ABACABADEDF")
print (numberSegments(s))   # print 3
