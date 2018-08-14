class Solution:
    def findRestaurant(self, list1, list2):
        """
        Optimal solution for this problem.
        1) Loop through list1 to find index of all items.
        2) Loop through list2 to check if same item exists and calculate index sum.
        3) At the same time finding minimum index sum.
        O(l1 + l2) run-time.
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        res = collections.defaultdict(list)
        for ix, item in enumerate(list1):
            d[item] = ix

        min_ = sys.maxsize

        for ix, item in enumerate(list2):
            if item in d:
                if ix + d[item] < min_:
                    min_ = ix + d[item]
                    res[min_].append(item)
                elif ix + d[item] == min_:
                    res[min_].append(item)
        return res[min_]
