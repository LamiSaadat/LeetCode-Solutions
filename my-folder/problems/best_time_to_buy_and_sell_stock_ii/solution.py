class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if len(prices) == 1:
            return profit

        for i in range(len(prices)):
            if i == len(prices) - 2:
                if prices[i] < prices[i+1]:
                    profit += prices[i+1] - prices[i]
                return profit
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
                i+=2
            else:
                i+=1
        return profit