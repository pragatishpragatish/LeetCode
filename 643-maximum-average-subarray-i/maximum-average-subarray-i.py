class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        iSum = sum(nums[:k])
        maxSum = iSum
        for i in range(k, len(nums)):
            iSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, iSum)
        return maxSum/k