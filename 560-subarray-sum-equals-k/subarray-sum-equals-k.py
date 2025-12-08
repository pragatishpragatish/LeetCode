class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0:1}
        count = 0
        tsum = 0
        for i in range(len(nums)):
            tsum += nums[i]
            diff = tsum - k
            if diff in hash:
                count += hash[diff]

            hash[tsum] = hash.get(tsum, 0) + 1

        return count