# The most confusing part of this problem is how to understand lexicographically sorted words.
# Only consider two adjacent words at a time.
class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words == None or len(words) == 0: return ""
        graph = collections.defaultdict(set)     # set of characters depend on it
        q = collections.deque()
        indegrees = {}
        
        for word in words:
            for c in word:
                indegrees[c] = 0
        
        for x, y in zip(words, words[1:]):
            max_len = min(len(x), len(y))
            for i in range(max_len):
                if x[i] != y[i]:
                    if y[i] not in graph[x[i]]:
                        graph[x[i]].add(y[i])
                        if y[i] in indegrees:
                            indegrees[y[i]] += 1
                        else:
                            indegrees[y[i]] = 1
                    break

        for k in indegrees:
            if indegrees[k] == 0:    
                q.append(k)

        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for neighbor in graph[cur]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        return ''.join(res) if len(res) == len(graph) else ""
