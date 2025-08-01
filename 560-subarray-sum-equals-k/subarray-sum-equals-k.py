class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        tsum = 0
        map = {0: 1}

        for num in nums:
            tsum += num
            count += map.get(tsum - k, 0)
            map[tsum] = map.get(tsum, 0) + 1

        return count