class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [1] * n
        prefix[0], postfix[-1] = nums[0], nums[-1]

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i-1]

        for i in range(n-2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]

        for i in range(n):
            if i>0 and i<n-1:
                res[i] = prefix[i-1] * postfix[i+1]        
            if i == 0:
                res[i] = postfix[i+1]
            if i == n-1:
                res[i] = prefix[i-1]
        return res
        print(prefix, postfix)