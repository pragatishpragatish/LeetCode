class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        iniCol = image[sr][sc]
        if iniCol == color:
            return image
        seen = set()

        def dfs(r,c):            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if (r,c) in seen:
                return
            seen.add((r,c))
            if image[r][c] != iniCol:
                return
            image[r][c] = color

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if (r+dr, c+dc) not in seen:
                    dfs(r+dr, c+dc)

        dfs(sr, sc)
        return image