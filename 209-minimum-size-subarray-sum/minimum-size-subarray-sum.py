class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        left = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                minLength = min(minLength, i-left+1)
                total -= nums[left]
                left += 1

        return 0 if minLength == float('inf') else minLength