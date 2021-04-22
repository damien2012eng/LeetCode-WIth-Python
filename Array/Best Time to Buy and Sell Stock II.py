class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total, temp = 0, 0
        n = len(prices)
        if n < 2:
            return 0
        p1, p2 = 0, 1
        bought = False
        while p2 < n:
            if not bought:
                if prices[p1] < prices[p2]:
                    bought = True
                    temp = prices[p1]
            else:
                if prices[p1] > prices[p2]:
                    bought = False
                    total = total + prices[p1] - temp
            p1 += 1
            p2 += 1
        if bought:
            total = total + prices[-1] - temp
        return total
