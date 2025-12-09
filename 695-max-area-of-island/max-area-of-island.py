class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if (r, c) in seen or grid[r][c] != 1:
                return 0
            seen.add((r, c))
            
            area = 1
            
            dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dire:
                area += dfs(r+dr, c+dc)
            
            return area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == 1:
                    maxA = max(maxA, dfs(r, c))

        return maxA