class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0

        for i in range(len(prices)):
            minP = min(minP, prices[i])
            maxP = max(maxP, prices[i] - minP)

        return maxP