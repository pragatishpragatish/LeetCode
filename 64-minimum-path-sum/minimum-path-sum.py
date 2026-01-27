class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        INF = float("inf")
        res = []

        for i in range(rows + 1):
            res.append([INF] * (cols+1))

        res[rows][cols-1] = 0

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])

        return res[0][0]