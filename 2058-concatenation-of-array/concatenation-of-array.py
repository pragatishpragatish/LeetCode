class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for n in nums:
            res.append(n)

        for n in nums:
            res.append(n)

        return res