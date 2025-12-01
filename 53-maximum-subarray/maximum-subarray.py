class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for x in nums:
            currSum = max(currSum+x, x)
            maxSum = max(currSum, maxSum)

        return maxSum