class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        iniCol = image[sr][sc]
        if iniCol == color:
            return image

        seen = set()
        rows, cols = len(image), len(image[0])

        def dfs(r,c):
            if (r, c) in seen:
                return
            seen.add((r, c))
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if image[r][c] != iniCol:
                return
            
            image[r][c] = color

            dire = [[1,0], [-1,0], [0,1], [0,-1]]
            for dc, dr in dire:
                dfs(r+dr, c+dc)

        dfs(sr, sc)
        return image