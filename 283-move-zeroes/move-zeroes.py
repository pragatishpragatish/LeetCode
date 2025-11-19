class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iPos = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[iPos] = nums[i]
                iPos += 1
        
        for j in range(iPos, n):
            nums[j] = 0