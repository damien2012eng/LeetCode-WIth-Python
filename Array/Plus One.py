class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #Simple case (last digit is not 9)
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        #Initialization
        i = 1
        n = len(digits)
        #While loop
        while i <= n and digits[-i] == 9:
            digits[-i]=0
            i+=1
        #Special case (All 9s)
        if i == n+1:
            return [1]+digits
        #Rest of cases
        else:
            digits[-i] = digits[-i] + 1
            return digits
