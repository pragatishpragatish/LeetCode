class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        print(numSet)
        return not len(numSet) == len(nums)