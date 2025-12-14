class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def fib(n):
            if n == 1:
                return 1
            
            if n == 2:
                return 2
            
            if n in memo:
                return memo[n]
            memo[n] = fib(n-1) + fib(n-2)

            return fib(n-1) + fib(n-2)
        return fib(n)