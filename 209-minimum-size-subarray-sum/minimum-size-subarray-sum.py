class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        minLen = float("inf")
        currSum = 0
        for r in range(n):
            currSum += nums[r]

            while currSum >= target:
                minLen = min(minLen, (r-l+1))
                currSum -= nums[l]
                l += 1

        return 0 if minLen == float("inf") else minLen