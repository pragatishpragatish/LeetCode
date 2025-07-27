class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = nums[0]
        for n in nums[1:]:
            currSum = max(n, currSum + n)
            maxSum = max(maxSum, currSum)
        return maxSum