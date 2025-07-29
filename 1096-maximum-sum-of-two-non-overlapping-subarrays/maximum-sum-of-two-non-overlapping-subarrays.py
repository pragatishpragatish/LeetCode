class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        def maxSum(A, L, M):
            n = len(A)
            prefix = [0] * (n+1)
            for i in range(n):
                prefix[i+1] = prefix[i] + A[i]

            max_L = 0
            result = 0
            for i in range(L + M, n+1):
                max_L = max(max_L, prefix[i - M] - prefix[i - M - L])
                result = max(result, max_L + prefix[i] - prefix[i - M])
            return result
        
        return max(maxSum(nums, firstLen, secondLen), maxSum(nums, secondLen, firstLen))
