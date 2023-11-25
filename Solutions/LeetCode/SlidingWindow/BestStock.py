class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = r = maxPrice = 0
        lenPrices = len(prices)

        while r < lenPrices:
            if prices[r] < prices[l]:
                l = r
            maxPrice = max(maxPrice, prices[r] - prices[l])
            r += 1
        
        return maxPrice
            

        