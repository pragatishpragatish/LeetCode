class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        se = set(nums)
        n = len(nums)
        res = []
        for i in range(1,n+1):
            if i not in se:
                res.append(i)
        return res