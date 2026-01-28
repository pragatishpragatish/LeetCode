class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if (r, c) in seen:
                return
            seen.add((r, c))

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] != "1":
                return

            dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in dire:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count