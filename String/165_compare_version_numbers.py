class Solution:
    def compareVersion(self, version1, version2):
        """
        great problem to think about corner cases.
        what if two versions are same for mutual depth but longer one has '0.0.0' postfix?
        e.g. '1.0.0.1.0.0', '1.0.0.1'


        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        for x, y in zip(v1, v2):
            if int(x) > int(y):
                return 1
            elif int(x) < int(y):
                return -1

        # all prefixes are equal
        if len(v1) > len(v2):
            for num in v1[len(v2):]:
                if int(num) > 0:
                    return 1
        elif len(v1) < len(v2):
            for num in v2[len(v1):]:
                if int(num) > 0:
                    return -1
        return 0
