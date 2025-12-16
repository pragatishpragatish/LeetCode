class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tSum = sum(nums)
        half = tSum / 2
        seen = set()
        seen.add(0)
        
        for i in range(len(nums)-1, -1, -1):
            if half in seen:
                return True
            temp = []
            for x in seen:
                temp.append(x+nums[i])
            while temp:
                seen.add(temp.pop())
        print(half)
        print(seen)
        return False