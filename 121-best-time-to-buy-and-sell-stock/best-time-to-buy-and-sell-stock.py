class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPri = prices[0]

        for x in prices:
            minPri = min(minPri, x)
            maxProf = max(maxProf, x-minPri)

        return maxProf