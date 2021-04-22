class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #S1 Sort the list
        nums.sort()
        #S2 Initialize
        half = len(nums)//2
        #For loop
        for i in range(half):
            if nums[i*2] != nums[i*2+1]:
                return nums[i*2]
        return nums[-1]
