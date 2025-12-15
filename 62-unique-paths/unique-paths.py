class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = []
        for _ in range(m+1):
            res.append([0] * (n + 1))
        res[m-1][n-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i != (m-1) or j != (n-1):
                    res[i][j] = res[i][j+1] + res[i+1][j]

        return res[0][0]