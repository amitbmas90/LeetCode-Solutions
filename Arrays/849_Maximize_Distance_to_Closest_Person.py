class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        temp = []
        MIN_ = -sys.maxsize
        MAX_ = sys.maxsize
        left_closest, right_closest = -1, -1
        for ii, seat in enumerate(seats):
            if seat == 1:
                left_closest = ii
                temp.append(-1)
            else:
                if left_closest >= 0:
                    temp.append(ii - left_closest)
                else:
                    temp.append(MAX_)

        res = MIN_
        temp = temp[::-1]
        for ii, seat in enumerate(seats[::-1], 0):
            if seat == 1:
                right_closest = ii
            else:
                if right_closest >= 0:
                    res = max(res, min(temp[ii], ii - right_closest))
                else:
                    res = max(res, temp[ii])
        return res
