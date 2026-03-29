class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minprice = prices[0]
        for price in prices:
            maxProfit = max(maxProfit, price - minprice)
            minprice = min(price,minprice)
        return maxProfit

            