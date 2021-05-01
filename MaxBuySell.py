class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        
        max_profit = 0
        index = 1;
        
        # Brute force approach, iterate through every combination and 
        # check if price is greater than the max profit, only check
        # sell conditions that happen after the buy
        for buy_price in prices:
            for sell_index in range(index, len(prices)):
                if prices[sell_index] - buy_price >  max_profit:
                    max_profit = prices[sell_index] - buy_price
            index = index + 1
        
        return max_profit
