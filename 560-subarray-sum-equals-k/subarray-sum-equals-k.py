class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        map = {0: 1}
        count = 0
        for i in nums:
            total += i
            if (total - k) in map:
                count += map[total - k]

            map[total] = map.get(total, 0) + 1
        return count