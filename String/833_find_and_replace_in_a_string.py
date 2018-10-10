class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = []
        s_ix = 0  # index of original string up to which has been processed

        m = {index: ix for ix, index in enumerate(indexes)}
        indexes.sort()

        for ix in indexes:
            source = sources[m[ix]]
            target = targets[m[ix]]
            l = len(source)
            if S[ix: ix + l] == source:
                res.append(S[s_ix: ix])
                res.append(target)
                s_ix = ix + l

        res.append(S[s_ix: len(S)])
        return ''.join(res)
