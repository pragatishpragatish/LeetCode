class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for i in range(n):
            dif = target - nums[i]
            if dif in seen:
                return [seen[dif], i]
            seen[nums[i]] = i
        return []