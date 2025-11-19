class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxCap = 0

        while l<r:
            h = min(height[l], height[r])
            length = r-l
            area = h*length
            maxCap = max(area, maxCap)
            
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return maxCap