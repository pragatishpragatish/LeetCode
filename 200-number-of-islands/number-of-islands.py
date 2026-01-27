class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            if (r, c) in seen:
                return
            seen.add((r, c))
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != "1":
                return

            dire = [[1,0],[-1,0],[0,1],[0,-1]]
            for i in range(len(dire)):
                dr, dc = dire[i]
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands