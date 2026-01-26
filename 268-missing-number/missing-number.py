class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arrXOR = 0
        for x in nums:
            arrXOR ^= x

        for i in range(n+1):
            arrXOR ^= i

        return arrXOR
            