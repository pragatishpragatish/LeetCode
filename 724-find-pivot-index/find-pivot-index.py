class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lSum = 0

        for i, x in enumerate(nums):
            if lSum == total - lSum - x:
                return i
            lSum += x

        return -1