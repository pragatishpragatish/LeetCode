class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in map:
                return [map[rem], i]
            map[num] = i