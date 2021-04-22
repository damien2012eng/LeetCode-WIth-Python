class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = []
        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                return True
        return False
