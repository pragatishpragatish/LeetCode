class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        ans = []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in map:
                ans.append(map.get(rem))
                ans.append(i)
            map[nums[i]] = i

        return ans