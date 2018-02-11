# O(Aα(A))≈O(A) Run-time
# O(N) space complexity, where N is total number of emails
# 284 ms, beat 75%
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        count, email_to_id, email_to_name, groups = 0, {}, {}, []
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = count
                    groups.append(count)
                    count += 1
                    
        def find(x):
            if groups[x] == x:
                return x
            return find(groups[x])
        
        def union(x, y):
            gx = find(x)
            gy = find(y)
            if gx != gy:
                if rank[gx] < rank[gy]:
                    groups[gx] = gy
                elif rank[gx] > rank[gy]:
                    groups[gy] = gx
                else:
                    rank[gx] += 1
                    groups[gy] = gx
        
        rank = [0] * count 
        for account in accounts:
            head = account[1]
            for email in account[2:]:
                union(email_to_id[head], email_to_id[email])
                
        res = collections.defaultdict(list)
        rev_m = {idx: email for email, idx in email_to_id.items()}
        for i, g in enumerate(groups):
            res[find(g)].append(rev_m[i])
        return [[email_to_name[rev_m[g]]] + sorted(res[g]) for g in res]
        
