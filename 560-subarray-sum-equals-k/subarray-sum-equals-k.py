class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = {0:1}
        pSum = 0
        for num in nums:
            pSum += num
            if (pSum - k) in prefix:
                count += prefix[pSum - k]
            prefix[pSum] = prefix.get(pSum, 0) + 1
        return count
        #{0:3. 1:1,}
