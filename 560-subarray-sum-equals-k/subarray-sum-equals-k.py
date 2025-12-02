class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hash = {0:1}
        pSum = 0

        for num in nums:
            pSum += num
            diff = pSum-k
            if diff in hash:
                count += hash[diff]
            hash[pSum] = hash.get(pSum, 0) + 1
        return count