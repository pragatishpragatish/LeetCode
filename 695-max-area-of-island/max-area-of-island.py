class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] != 1 or (r,c) in visit:
                return 0

            visit.add((r,c))
            area = 1

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(dfs(r,c), maxArea)

        return maxArea