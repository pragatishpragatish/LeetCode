class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        if grid[r-1][c-1] == 1:
            return 0
        res = []

        for _ in range(r+1):
            res.append([0] * (c+1))

        res[r-1][c-1] = 1

        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if grid[i][j] == 1:
                    res[i][j] = 0
                    continue
                if i != (r-1) or j != (c-1):
                    res[i][j] = res[i+1][j] + res[i][j+1]

        return res[0][0]