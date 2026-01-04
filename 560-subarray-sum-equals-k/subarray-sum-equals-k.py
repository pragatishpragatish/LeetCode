class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0: 1}
        tsum = 0
        count = 0

        for x in nums:
            tsum += x
            diff = tsum - k
            if diff in hash:
                count += hash[diff]

            hash[tsum] = hash.get(tsum, 0) + 1
        return count