class Solution:
    def floodFill(self, images: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(images), len(images[0])
        start_color = images[sr][sc]

        if start_color == color:
            return images

        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return

            if images[r][c] != start_color:
                return
            
            images[r][c] = color

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr, sc)
        return images