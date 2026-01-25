class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tSum = 0
        minLen = float("inf")
        l = 0

        for r in range(len(nums)):
            tSum += nums[r]

            while tSum >= target:
                minLen = min(minLen, (r-l+1))
                tSum -= nums[l]
                l += 1
        return 0 if minLen == float("inf") else minLen