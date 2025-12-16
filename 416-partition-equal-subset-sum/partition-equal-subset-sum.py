class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tSum = sum(nums)
        if tSum%2 != 0:
            return False
        half = tSum // 2
        seen = {0}

        for i in range(len(nums)-1, -1, -1):
            if half in seen:
                return True
            temp = []
            for x in seen:
                temp.append(x+nums[i])

            while temp:
                seen.add(temp.pop())

        return False