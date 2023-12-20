def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_i=0
        sell_i=1
        cur_max=0
        while sell_i <= len(prices)-1:                      # Moving Window
            cur_profit = prices[sell_i] - prices[buy_i]     # Calculate current profit
            if cur_profit > cur_max:                        # Replace maximum profit if larger
                cur_max = cur_profit
            if prices[sell_i] <= prices[buy_i]:             # Reset window if smaller buy point found
                buy_i = sell_i
            sell_i+=1                                       # Move window start forward
        return cur_max
