class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        
        for x in nums:
            currSum = max(currSum + x, x)
            maxSum = max(maxSum, currSum)

        return maxSum