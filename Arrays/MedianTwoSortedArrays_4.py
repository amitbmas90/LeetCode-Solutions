class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2: return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        l, r = 0, n1
        while l < r:
            m1 = l + (r-l) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = k - m1

        candidate1 = max(nums1[m1-1] if m1 > 0 else -sys.maxsize, nums2[m2-1] if m2 > 0 else -sys.maxsize)
        
        if (n1 + n2) % 2 == 1:
            return candidate1 / 1.0
        
        candidate2 = min(nums1[m1] if m1 < n1 else sys.maxsize, nums2[m2] if m2 < n2 else sys.maxsize)
        
        return (candidate1 + candidate2)/2
