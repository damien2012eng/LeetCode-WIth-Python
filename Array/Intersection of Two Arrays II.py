class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Sort both lists
        nums1.sort()
        nums2.sort()
        #Initialization
        p1,p2 = 0,0
        ret = []
        n1, n2 = len(nums1), len(nums2)
        #While loop
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                ret.append(nums1[p1])
                p1 += 1
                p2 += 1
        return ret
