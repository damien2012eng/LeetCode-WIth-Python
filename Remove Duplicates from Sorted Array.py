class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Main branch
        #Initialization
        #Bugfix branch
        n = len(nums)
        if n == 0:
            return 0
        p1, p2 = 0, 1
        #While loop with two pointers
        while p2 < n:
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1
        return p1+1
