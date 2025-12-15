class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = []
        for _ in range(rows + 1):
            res.append([float("inf")] * (cols + 1))

        res[rows - 1][cols] = 0

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                res[i][j] = grid[i][j] + min(res[i][j+1], res[i+1][j])   

        return res[0][0]     
        print(res)