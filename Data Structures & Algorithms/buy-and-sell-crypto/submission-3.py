class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuyPrice = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            currentProfit = prices[i] - minBuyPrice
            maxProfit = max(currentProfit,maxProfit)
            minBuyPrice = min(prices[i],minBuyPrice)
        return maxProfit