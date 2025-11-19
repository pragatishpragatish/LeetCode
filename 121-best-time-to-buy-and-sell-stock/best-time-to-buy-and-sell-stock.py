class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0

        for x in prices:
            minPrice = min(minPrice, x)
            profit = x - minPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit