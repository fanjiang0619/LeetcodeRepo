class Solution:
    def maxProfit(self, prices):
        buy = 0
        profit = 0
        sell_max = 0
        for i in range(len(prices)-1):
            sell = i+1
            if prices[buy] < prices[sell] and prices[sell] > prices[sell_max]:
                sell_max = sell
            elif prices[buy] < prices[sell] and prices[sell] <= prices[sell_max]:
                profit += prices[sell_max] - prices[buy]
                buy = sell_max + 1
                sell_max = buy
            else:
                profit += prices[sell_max] - prices[buy]
                buy = sell
                sell_max = sell
        if sell_max > buy:
            profit += prices[sell_max] - prices[buy]
        
        return profit