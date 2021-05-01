class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        
        max_profit = 0
        # max int value
        minprice = sys.maxint
        
        # one pass with checking min against max values
        for item in prices:
            if item < minprice:
                minprice = item
            elif item - minprice > max_profit:
                max_profit = item - minprice
        
        return max_profit
