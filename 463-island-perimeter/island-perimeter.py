class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            if r >= rows or r < 0 or c < 0 or c >= cols:
                return 1

            if (r, c) in seen:
                return 0

            if grid[r][c] != 1:
                return 1
            seen.add((r, c))

            peri = 0

            dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dire:
                peri += dfs(r+dr, c+dc)

            return peri


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == 1:
                    perimeter += dfs(r, c)

        return perimeter