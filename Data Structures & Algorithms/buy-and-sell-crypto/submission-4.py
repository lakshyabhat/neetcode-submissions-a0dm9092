class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice,maxProfit = max(prices), 0
        for price in prices:
            maxProfit = max(price - minPrice,maxProfit)
            minPrice = min(minPrice,price)
        return maxProfit
