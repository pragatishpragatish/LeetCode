from collections import Counter
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0
        count0, count1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                count0 += 1
            diff = count0-count1
            if diff not in hashmap:
                hashmap[diff] = i
            
            if count0 == count1:
                res = max(res, count0+count1)
            else:
                idx = hashmap[diff]
                res = max(res, i-idx)

        return res